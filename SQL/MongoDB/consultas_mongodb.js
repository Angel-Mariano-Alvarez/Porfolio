
// 📦 Importación de datos
// mongoimport --db librosDB --collection libros --file libros.json --jsonArray

// 📘 Consultas requeridas:

// 1. Libros publicados antes de 1950
db.libros.find({ anioPublicacion: { $lt: 1950 } });

// 2. Libros del género "Fantasía"
db.libros.find({ genero: "Fantasia" });

// 3. Libros escritos por "J.R.R. Tolkien"
db.libros.find({ autores: "J.R.R. Tolkien" });

// 4. Número de libros por género
db.libros.aggregate([
  { $group: { _id: "$genero", total: { $sum: 1 } } }
]);

// 📤 Exportación de libros de Fantasía a JSON
// mongoexport --db librosDB --collection libros --query '{"genero": "Fantasia"}' --out libros_fantasia.json
