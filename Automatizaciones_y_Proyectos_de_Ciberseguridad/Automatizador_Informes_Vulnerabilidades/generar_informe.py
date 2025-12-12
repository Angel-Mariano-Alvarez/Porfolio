#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Informes de Vulnerabilidades 

"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta
from pathlib import Path
import sys
import os
import json
import time
import requests
import re
import html
import traceback
import functools
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn
from docx.enum.section import WD_SECTION_START

# Intentar importar librerías opcionales
try:
    from googletrans import Translator
    TRANSLATOR_DISPONIBLE = True
    translator_global = Translator()
except ImportError:
    TRANSLATOR_DISPONIBLE = False
    translator_global = None

# Configurar matplotlib para no usar interfaz gráfica
matplotlib.use('Agg')

# API Key desde variables de entorno
NVD_API_KEY = os.getenv('NVD_API_KEY', None)

if NVD_API_KEY:
    print("[INFO] API Key de NVD detectada.")
else:
    print("[WARN] Sin API Key de NVD - usando límite de peticiones públicas.")


# --- FUNCIONES AUXILIARES ---

def escapar_caracteres_xml(texto):
    """Escapa caracteres que pueden romper el XML de Word"""
    if not texto: return ""
    return texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")

def traducir_a_español(texto):
    """Traduce texto al español si la librería está disponible"""
    if not TRANSLATOR_DISPONIBLE or not texto or len(texto) < 5:
        return texto
    
    try:
        detection = translator_global.detect(texto)
        if detection.lang != 'es':
            resultado = translator_global.translate(texto, dest='es')
            return resultado.text
        return texto
    except:
        return texto

def log_tiempo_ejecucion(func):
    """Decorador para medir tiempos y capturar errores"""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        inicio = time.time()
        try:
            resultado = func(self, *args, **kwargs)
            duracion = time.time() - inicio
            if hasattr(self, 'metricas_red'):
                self.metricas_red['tiempo_total_consultas'] += duracion
            if duracion > 2:
                print(f"[TIME] {func.__name__} tardó {duracion:.2f}s")
            return resultado
        except Exception as e:
            duracion = time.time() - inicio
            if hasattr(self, 'metricas_red'):
                self.metricas_red['errores_red'] += 1
                self.metricas_red['tiempo_total_consultas'] += duracion
            print(f"[ERROR] Error en {func.__name__}: {str(e)}")
            return None
    return wrapper


# --- CLASES ---

class BuscadorCVERobusto:
    """Busca detalles de CVEs con caché y reintentos"""
    def __init__(self):
        self.cache_file = "cves_cache.json"
        self.cache_expiracion_dias = 30
        self.cache = self._cargar_cache()
        self.tiene_api_key = NVD_API_KEY is not None
        
        self.metricas_red = {
            'tiempo_total_consultas': 0.0,
            'exitos_nvd': 0,
            'fallbacks_cvedetails': 0,
            'fallbacks_generico': 0,
            'errores_red': 0
        }
        self._limpiar_cache_expirado()
        
    def _cargar_cache(self):
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _limpiar_cache_expirado(self):
        if not self.cache: return
        ahora = datetime.now()
        limite = ahora - timedelta(days=self.cache_expiracion_dias)
        cache_limpio = {}
        
        for cve_id, info in self.cache.items():
            try:
                if 'timestamp' in info and datetime.fromisoformat(info['timestamp']) >= limite:
                    cache_limpio[cve_id] = info
            except:
                pass
        
        if len(cache_limpio) < len(self.cache):
            self.cache = cache_limpio
            self._guardar_cache()
    
    def _guardar_cache(self):
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, ensure_ascii=False, indent=2)
        except: pass
    
    def _sanitizar_html(self, texto):
        if not texto: return ""
        texto = html.unescape(texto)
        texto = re.sub(r'<br\s*/?>', ' ', texto, flags=re.IGNORECASE)
        texto = re.sub(r'<[^>]+>', '', texto)
        return re.sub(r'\s+', ' ', texto).strip()

    def _limpiar_source(self, source_raw):
        """Limpia el identificador de fuente (ej: secure@microsoft.com -> Microsoft)"""
        if not source_raw: return "N/A"
        
        # Si es un email, coger el dominio
        if "@" in source_raw:
            try:
                dominio = source_raw.split("@")[1] # microsoft.com
                nombre = dominio.split(".")[0]     # microsoft
                
                # Casos especiales comunes
                if nombre == "mitre": return "MITRE"
                if nombre == "nist": return "NIST"
                
                return nombre.capitalize()
            except:
                return source_raw
        return source_raw

    @log_tiempo_ejecucion
    def _buscar_nvd(self, cve_id):
        """Busca en NVD y devuelve (descripcion, source)"""
        url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        if self.tiene_api_key:
            headers['apiKey'] = NVD_API_KEY
        
        for intento in range(3):
            try:
                response = requests.get(url, headers=headers, timeout=15)
                if response.status_code == 200:
                    data = response.json()
                    if 'vulnerabilities' in data and len(data['vulnerabilities']) > 0:
                        vuln = data['vulnerabilities'][0]['cve']
                        
                        # Obtener Source (Fuente)
                        source_raw = vuln.get('sourceIdentifier', 'NVD')
                        source_clean = self._limpiar_source(source_raw)
                        
                        # Obtener Descripción
                        desc_final = ""
                        if 'descriptions' in vuln:
                            for desc in vuln['descriptions']:
                                if desc['lang'] == 'es':
                                    desc_final = self._sanitizar_html(desc['value'])
                                    break
                            if not desc_final and len(vuln['descriptions']) > 0:
                                desc_final = self._sanitizar_html(vuln['descriptions'][0]['value'])
                        
                        if desc_final:
                            self.metricas_red['exitos_nvd'] += 1
                            return (desc_final, source_clean)
                
                return None
            except requests.exceptions.Timeout:
                time.sleep(0.5 * (2 ** intento))
            except:
                time.sleep(0.5)
        return None
    
    @log_tiempo_ejecucion
    def _buscar_cve_details(self, cve_id):
        """Fallback a CVE Details"""
        url = f"https.www.cvedetails.com/cve/{cve_id}/"
        for intento in range(3):
            try:
                response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
                if response.status_code == 200 and len(response.text) > 1000:
                    match = re.search(r'<b>Description:</b>\s*</td>\s*<td[^>]*>\s*([^<]+)', response.text)
                    if match:
                        self.metricas_red['fallbacks_cvedetails'] += 1
                        return self._sanitizar_html(match.group(1).strip())
            except:
                time.sleep(0.5)
        return None
    
    def _generar_descripcion_generica(self, cve_id, package_name=""):
        patrones = {
            'firefox': 'Vulnerabilidad de seguridad en Mozilla Firefox.',
            'teams': 'Vulnerabilidad en Microsoft Teams.',
            'chrome': 'Vulnerabilidad de seguridad en Google Chrome.',
            'edge': 'Vulnerabilidad en Microsoft Edge.',
            'office': 'Vulnerabilidad en Microsoft Office.',
            'windows': 'Vulnerabilidad de seguridad del sistema Windows.',
            'java': 'Vulnerabilidad en Java.',
        }
        package_lower = package_name.lower() if package_name else ''
        for patron, desc in patrones.items():
            if patron in package_lower:
                self.metricas_red['fallbacks_generico'] += 1
                return desc
        self.metricas_red['fallbacks_generico'] += 1
        return "Vulnerabilidad de seguridad identificada."
    
    def buscar_cve_nvd(self, cve_id, package_name=""):
        """Busca CVE: Cache -> NVD -> CVE Details -> Genérico"""
        
        # 1. Caché
        if cve_id in self.cache:
            cached = self.cache[cve_id]
            if cached.get('detalle'):
                cached['detalle'] = traducir_a_español(cached['detalle'])
            return cached
        
        info = {
            'cve_id': cve_id,
            'detalle': '',
            'origen': '',
            'source': 'N/A',  # Campo nuevo para la Fuente
            'url': f'https://nvd.nist.gov/vuln/detail/{cve_id}',
            'timestamp': datetime.now().isoformat()
        }
        
        # 2. NVD (Ahora devuelve tupla: detalle, source)
        resultado_nvd = self._buscar_nvd(cve_id)
        if resultado_nvd:
            detalle, source = resultado_nvd
            info['detalle'] = traducir_a_español(detalle)
            info['source'] = source
            info['origen'] = 'NVD'
        else:
            # 3. Fallback CVE Details
            detalle = self._buscar_cve_details(cve_id)
            if detalle:
                info['detalle'] = traducir_a_español(detalle)
                info['origen'] = 'CVE Details'
                info['source'] = 'CVE Details'
            else:
                # 4. Genérico
                detalle = self._generar_descripcion_generica(cve_id, package_name)
                info['detalle'] = detalle
                info['origen'] = 'Genérico'
                info['source'] = 'Automático'
        
        self.cache[cve_id] = info
        self._guardar_cache()
        return info


class GeneradorInformeDocx:
    def __init__(self, ruta_excel, infraestructura="Sistema", mes_anio=None):
        self.ruta_excel = ruta_excel
        self.infraestructura = infraestructura
        self.mes_anio = mes_anio if mes_anio else datetime.now().strftime("%B %Y")
        
        self.df = None
        self.metricas = {}
        self.rutas_graficos = []
        self.buscador = BuscadorCVERobusto()
    
    def cargar_datos(self):
        print(f"[INFO] Cargando datos: {self.ruta_excel}")
        try:
            self.df = pd.read_excel(self.ruta_excel, skiprows=1)
            self.df.columns = ['timestamp', 'host', 'cve', 'severity', 'package_name', 'package_version', 'status']
            print(f"[INFO] {len(self.df)} registros cargados")
        except Exception as e:
            print(f"[ERROR] Fallo al leer Excel: {e}")
            sys.exit(1)
    
    def calcular_metricas(self):
        print("[INFO] Calculando métricas...")
        self.metricas['total_vulnerabilities'] = len(self.df)
        self.metricas['unique_cves'] = self.df['cve'].nunique()
        self.metricas['unique_hosts'] = self.df['host'].nunique()
        
        severity_counts = self.df['severity'].value_counts()
        self.metricas['critical'] = severity_counts.get('Critical', 0)
        self.metricas['high'] = severity_counts.get('High', 0)
        self.metricas['medium'] = severity_counts.get('Medium', 0)
        self.metricas['low'] = severity_counts.get('Low', 0)
        
        total = self.metricas['total_vulnerabilities']
        for sev in ['critical', 'high', 'medium', 'low']:
            count = self.metricas[sev]
            self.metricas[f'{sev}_pct'] = round((count / total * 100), 2) if total > 0 else 0
    
    def generar_top_hosts(self):
        print("[INFO] Generando top hosts...")
        top_hosts = self.df.groupby('host').size().sort_values(ascending=False).head(5)
        datos = []
        for host in top_hosts.index:
            h_df = self.df[self.df['host'] == host]
            datos.append({
                'Host': host,
                'Total': len(h_df),
                'Críticas': len(h_df[h_df['severity'] == 'Critical']),
                'Altas': len(h_df[h_df['severity'] == 'High']),
                'Medias': len(h_df[h_df['severity'] == 'Medium']),
                'Bajas': len(h_df[h_df['severity'] == 'Low'])
            })
        self.metricas['top_hosts_data'] = pd.DataFrame(datos)
    
    def generar_top_cves(self):
        print("[INFO] Generando top CVEs...")
        top_cves = self.df.groupby('cve').size().sort_values(ascending=False).head(5)
        datos = []
        for cve in top_cves.index:
            c_df = self.df[self.df['cve'] == cve]
            datos.append({
                'CVE': cve,
                'Ocurrencias': len(c_df),
                'Severidad': c_df['severity'].mode()[0],
                'Hosts': c_df['host'].nunique()
            })
        self.metricas['top_cves_data'] = pd.DataFrame(datos)
    
    def generar_graficos(self):
        print("[INFO] Generando gráficos...")
        temp_dir = Path("temp_graficos")
        temp_dir.mkdir(exist_ok=True)
        self.rutas_graficos = []
        
        # 1. Pastel Severidad (Estilo Mejorado)
        fig, ax = plt.subplots(figsize=(10, 6))
        labels = ['Crítica', 'Alta', 'Media', 'Baja']
        sizes = [self.metricas['critical'], self.metricas['high'], self.metricas['medium'], self.metricas['low']]
        colors = ['#d32f2f', '#ff9800', '#fdd835', '#4caf50']
        
        # Filtrar ceros
        datos = [(l, s, c) for l, s, c in zip(labels, sizes, colors) if s > 0]
        if datos:
            l, s, c = zip(*datos)
            total = sum(s)
            new_labels = [f"{lbl} ({sz/total*100:.1f}%)" for lbl, sz in zip(l, s)]
            
            ax.pie(s, labels=new_labels, colors=c, startangle=90, 
                   wedgeprops={'edgecolor': 'black', 'linewidth': 1.5},
                   textprops={'fontweight': 'bold', 'fontsize': 11})
            ax.set_title('Distribución por Severidad', fontsize=14, fontweight='bold', pad=30)
        
        plt.tight_layout()
        ruta = temp_dir / "distribucion.png"
        plt.savefig(ruta, dpi=300, bbox_inches='tight')
        plt.close()
        self.rutas_graficos.append(str(ruta))
        
        # 2. Top Hosts
        fig, ax = plt.subplots(figsize=(10, 6))
        top_h = self.df.groupby('host').size().sort_values(ascending=False).head(5)
        bars = ax.barh(range(len(top_h)), top_h.values, color='#1976d2')
        ax.set_yticks(range(len(top_h)))
        ax.set_yticklabels(top_h.index)
        ax.set_xlabel('Vulnerabilidades', fontsize=12, fontweight='bold')
        ax.set_title('Top 5 Hosts', fontsize=14, fontweight='bold')
        for bar in bars:
            ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f' {int(bar.get_width())}', va='center', fontweight='bold')
        plt.tight_layout()
        ruta = temp_dir / "hosts.png"
        plt.savefig(ruta, dpi=300, bbox_inches='tight')
        plt.close()
        self.rutas_graficos.append(str(ruta))
        
        # 3. Top CVEs
        fig, ax = plt.subplots(figsize=(10, 6))
        top_c = self.df.groupby('cve').size().sort_values(ascending=False).head(5)
        bars = ax.barh(range(len(top_c)), top_c.values, color='#f57c00')
        ax.set_yticks(range(len(top_c)))
        ax.set_yticklabels(top_c.index, fontsize=10)
        ax.set_xlabel('Ocurrencias', fontsize=12, fontweight='bold')
        ax.set_title('Top 5 CVEs Más Frecuentes', fontsize=14, fontweight='bold')
        for bar in bars:
            ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f' {int(bar.get_width())}', va='center', fontweight='bold')
        plt.tight_layout()
        ruta = temp_dir / "cves.png"
        plt.savefig(ruta, dpi=300, bbox_inches='tight')
        plt.close()
        self.rutas_graficos.append(str(ruta))

    def _procesar_lista_cves(self, severidad, prefijo):
        df_sev = self.df[self.df['severity'] == severidad]
        cves_unicos = df_sev['cve'].unique()
        lista = []
        
        if len(cves_unicos) > 0:
            print(f"[INFO] Procesando {len(cves_unicos)} CVEs {severidad}...")
            pausa = 6 if not self.buscador.tiene_api_key else 0.3
            
            for idx, cve in enumerate(cves_unicos):
                print(f"  [{prefijo}-{idx+1}/{len(cves_unicos)}] {cve}...", end=" ")
                cve_df = df_sev[df_sev['cve'] == cve]
                pkg = cve_df['package_name'].iloc[0] if len(cve_df) > 0 else ''
                
                info = self.buscador.buscar_cve_nvd(cve, pkg)
                
                lista.append({
                    'cve': cve,
                    'occurrences': len(cve_df),
                    'hosts_affected': cve_df['host'].nunique(),
                    'package_name': pkg,
                    'info': info
                })
                print("[OK]")
                time.sleep(pausa)
        return lista

    def generar_detalles_vulnerabilidades(self):
        print("[INFO] Buscando detalles de CVEs...")
        self.metricas['top_critical_cves'] = self._procesar_lista_cves('Critical', 'C')
        self.metricas['top_high_cves'] = self._procesar_lista_cves('High', 'H')
        self.metricas['top_medium_cves'] = self._procesar_lista_cves('Medium', 'M')
        self.metricas['top_low_cves'] = self._procesar_lista_cves('Low', 'L')
    
    def _add_table_with_data(self, doc, headers, data):
        table = doc.add_table(rows=1, cols=len(headers))
        table.style = 'Table Grid'
        for i, h in enumerate(headers):
            table.rows[0].cells[i].text = str(h)
        for row_d in data:
            row_cells = table.add_row().cells
            for i, v in enumerate(row_d):
                row_cells[i].text = str(v)
    
    def _agregar_cve_con_hipervinculo(self, doc, item):
        info = item['info']
        
        p = doc.add_paragraph()
        run = p.add_run(info['cve_id'])
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 139)
        
        doc.add_paragraph(f"Detalle técnico: {info['detalle']}")
        doc.add_paragraph(f"Ocurrencias: {item['occurrences']}")
        doc.add_paragraph(f"Hosts afectados: {item['hosts_affected']}")
        doc.add_paragraph(f"Paquete: {item['package_name']}")
        
        # --- NUEVO: Campo Fuente (Source) ---
        if info.get('source') and info['source'] != 'N/A':
            doc.add_paragraph(f"Fuente: {info['source']}")
        
        # Enlace Seguro (Field Codes)
        p_ref = doc.add_paragraph()
        p_ref.add_run("Referencia: ")
        
        try:
            url = info['url'].replace('"', '%22')
            
            # Field Codes para HYPERLINK
            run_begin = p_ref.add_run()
            fldChar_begin = OxmlElement('w:fldChar')
            fldChar_begin.set(qn('w:fldCharType'), 'begin')
            run_begin._r.append(fldChar_begin)
            
            run_instr = p_ref.add_run()
            instrText = OxmlElement('w:instrText')
            instrText.set(qn('xml:space'), 'preserve')
            instrText.text = f'HYPERLINK "{url}"'
            run_instr._r.append(instrText)
            
            run_sep = p_ref.add_run()
            fldChar_sep = OxmlElement('w:fldChar')
            fldChar_sep.set(qn('w:fldCharType'), 'separate')
            run_sep._r.append(fldChar_sep)
            
            run_disp = p_ref.add_run(info['url'])
            run_disp.font.color.rgb = RGBColor(0, 0, 255)
            run_disp.font.underline = True
            
            run_end = p_ref.add_run()
            fldChar_end = OxmlElement('w:fldChar')
            fldChar_end.set(qn('w:fldCharType'), 'end')
            run_end._r.append(fldChar_end)
            
        except:
            p_ref.add_run(info['url'])
        
        doc.add_paragraph()

    def _configurar_toc(self, doc):
        try:
            settings = doc.settings.element
            update = OxmlElement('w:updateFields')
            update.set(qn('w:val'), 'true')
            settings.append(update)
        except: pass

    def generar_docx(self, nombre_salida=None):
        print("[INFO] Generando DOCX...")
        
        # ---  FORMATO DE NOMBRE ---
        if nombre_salida is None:
            # Limpiar caracteres no válidos en nombre de archivo
            periodo_safe = self.mes_anio.replace('/', '-').replace('\\', '-')
            empresa_safe = self.infraestructura.replace('/', '-').replace('\\', '-')
            nombre_salida = f"INFORME_VULNERABILIDADES_{empresa_safe}_{periodo_safe}.docx"
        
        doc = Document()
        
        # 1. PORTADA
        section = doc.sections[0]
        section.top_margin = Inches(0)
        section.bottom_margin = Inches(0)
        section.left_margin = Inches(0)
        section.right_margin = Inches(0)
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        portada_path = os.path.join(script_dir, "imagenes", "portada.png")
        
        if os.path.exists(portada_path):
            try:
                doc.add_picture(portada_path, width=Inches(8.27))
                doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
            except:
                doc.add_heading("INFORME", 0)
        else:
            doc.add_heading("INFORME DE VULNERABILIDADES", 0)

        doc.add_section(WD_SECTION_START.NEW_PAGE)
        
        # 2. ÍNDICE
        section = doc.sections[-1]
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.footer.is_linked_to_previous = False
        
        t = doc.add_paragraph("INFORME DE VULNERABILIDADES")
        t.alignment = WD_ALIGN_PARAGRAPH.CENTER
        t.runs[0].font.size = Pt(16)
        t.runs[0].bold = True
        t.runs[0].underline = True
        
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run("Empresa: ").bold = True
        p.runs[0].font.size = Pt(16)
        p.add_run(self.infraestructura).font.size = Pt(16)
        
        p2 = doc.add_paragraph(f"{self.mes_anio}")
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.runs[0].font.size = Pt(14)
        p2.runs[0].font.bold = True
        
        doc.add_paragraph()
        
        pi = doc.add_paragraph()
        pi.add_run("Índice").font.size = Pt(18)
        pi.runs[0].bold = True
        
        # TOC Field Code
        p = doc.add_paragraph()
        r = p.add_run()
        fldChar = OxmlElement('w:fldChar')
        fldChar.set(qn('w:fldCharType'), 'begin')
        r._r.append(fldChar)
        instr = OxmlElement('w:instrText')
        instr.text = 'TOC \\o "1-1" \\h \\z \\u'
        r._r.append(instr)
        fldChar2 = OxmlElement('w:fldChar')
        fldChar2.set(qn('w:fldCharType'), 'end')
        r._r.append(fldChar2)
        
        doc.add_section(WD_SECTION_START.NEW_PAGE)
        
        # 3. CONTENIDO
        section = doc.sections[-1]
        section.footer.is_linked_to_previous = False
        
        # Pie de página
        sectPr = section._sectPr
        pgNumType = OxmlElement('w:pgNumType')
        pgNumType.set(qn('w:start'), "1")
        sectPr.append(pgNumType)
        
        footer = section.footer
        p_foot = footer.paragraphs[0]
        p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_foot.add_run("Página ")
        
        r = p_foot.add_run()
        fld = OxmlElement('w:fldChar')
        fld.set(qn('w:fldCharType'), 'begin')
        r._r.append(fld)
        instr = OxmlElement('w:instrText')
        instr.text = "PAGE"
        r._r.append(instr)
        fld2 = OxmlElement('w:fldChar')
        fld2.set(qn('w:fldCharType'), 'end')
        r._r.append(fld2)
        
        logo_path = os.path.join(script_dir, "imagenes", "logo.png")
        if os.path.exists(logo_path):
            pl = footer.add_paragraph()
            pl.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            run = pl.add_run()
            run.add_picture(logo_path, width=Inches(0.7))

        # Contenido Real
        doc.add_heading("Resumen Ejecutivo", 1)
        doc.add_paragraph(f"Durante el análisis de {self.mes_anio}, se identificaron {self.metricas['total_vulnerabilities']} vulnerabilidades en {self.metricas['unique_hosts']} hosts. Críticas: {self.metricas['critical']}, Altas: {self.metricas['high']}.")
        
        doc.add_paragraph()
        doc.add_heading("Métricas Generales", 2)
        metrics = [
            ["Total", str(self.metricas['total_vulnerabilities'])],
            ["CVEs Únicos", str(self.metricas['unique_cves'])],
            ["Hosts", str(self.metricas['unique_hosts'])],
            ["Críticas", str(self.metricas['critical'])],
            ["Altas", str(self.metricas['high'])],
            ["Medias", str(self.metricas['medium'])],
            ["Bajas", str(self.metricas['low'])]
        ]
        self._add_table_with_data(doc, ["Métrica", "Valor"], metrics)
        
        doc.add_page_break()
        
        doc.add_heading("Análisis por Severidad", 1)
        doc.add_paragraph("Distribución de vulnerabilidades por nivel de riesgo.")
        doc.add_paragraph()
        if len(self.rutas_graficos) > 0:
            doc.add_picture(self.rutas_graficos[0], width=Inches(5.5))
            
        doc.add_page_break()
        
        doc.add_heading("Análisis de Infraestructura", 1)
        doc.add_heading("Top 5 Hosts", 2)
        
        hosts_data = []
        for _, row in self.metricas['top_hosts_data'].iterrows():
            hosts_data.append([row['Host'], str(row['Total']), str(row['Críticas']), str(row['Altas']), str(row['Medias']), str(row['Bajas'])])
        self._add_table_with_data(doc, ['Host', 'Tot', 'Crit', 'Alt', 'Med', 'Baj'], hosts_data)
        
        doc.add_paragraph()
        if len(self.rutas_graficos) > 1:
            doc.add_picture(self.rutas_graficos[1], width=Inches(5.5))
            
        doc.add_page_break()
        
        doc.add_heading("Análisis de CVEs", 1)
        doc.add_heading("Top 5 CVEs", 2)
        
        cves_data = []
        for _, row in self.metricas['top_cves_data'].iterrows():
            cves_data.append([row['CVE'], str(row['Ocurrencias']), row['Severidad'], str(row['Hosts'])])
        self._add_table_with_data(doc, ['CVE', 'Ocur', 'Sev', 'Hosts'], cves_data)
        
        doc.add_paragraph()
        if len(self.rutas_graficos) > 2:
            doc.add_picture(self.rutas_graficos[2], width=Inches(5.5))
            
        # Detalles
        for sev, lista in [('Críticas', self.metricas['top_critical_cves']), 
                           ('Altas', self.metricas['top_high_cves']),
                           ('Medias', self.metricas['top_medium_cves']),
                           ('Bajas', self.metricas['top_low_cves'])]:
            if lista:
                doc.add_page_break()
                doc.add_heading(f"Vulnerabilidades {sev}", 1)
                for item in lista:
                    self._agregar_cve_con_hipervinculo(doc, item)
        
        self._configurar_toc(doc)
        
        try:
            doc.save(nombre_salida)
            print(f"[SUCCESS] Generado: {nombre_salida}")
        except PermissionError:
            print(f"[ERROR] No se pudo guardar. Cierra el archivo Word '{nombre_salida}' e inténtalo de nuevo.")
            return None
            
        # Limpieza
        try:
            for r in self.rutas_graficos: os.remove(r)
            os.rmdir("temp_graficos")
        except: pass
        
        return nombre_salida

    def ejecutar_completo(self):
        print("\n" + "="*70)
        print("  GENERADOR DE INFORMES ")
        print("="*70 + "\n")
        
        self.cargar_datos()
        self.calcular_metricas()
        self.generar_top_hosts()
        self.generar_top_cves()
        self.generar_detalles_vulnerabilidades()
        self.generar_graficos()
        
        self.generar_docx()
        
        print("\n" + "="*70)
        print("[FIN] Proceso completado.")
        print("="*70 + "\n")


def main():
    if len(sys.argv) < 2:
        print("Uso: python generar_informe.py <excel> [empresa] [periodo]")
        sys.exit(1)
    
    generador = GeneradorInformeDocx(sys.argv[1], 
                                     sys.argv[2] if len(sys.argv) > 2 else "Empresa", 
                                     sys.argv[3] if len(sys.argv) > 3 else None)
    generador.ejecutar_completo()

if __name__ == "__main__":
    main()