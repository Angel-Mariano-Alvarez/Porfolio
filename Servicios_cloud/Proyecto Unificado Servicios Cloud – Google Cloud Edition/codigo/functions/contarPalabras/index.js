// HTTP: POST { "texto": "hola mundo desde gcp" }
exports.contarPalabras = (req, res) => {
  try {
    const texto = ((req.body && req.body.texto) || "").trim();
    if (!texto) {
      return res.status(400).json({ error: "Falta 'texto' en el body" });
    }
    const palabras = texto.split(/\s+/).filter(Boolean).length;
    return res.status(200).json({ palabras });
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
};
