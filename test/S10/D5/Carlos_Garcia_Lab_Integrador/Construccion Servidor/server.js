const express = require('express');
const app = express();
app.use(express.json());

// Definimos los puertos
const PORT = 3000;

// Endpoint de saludo
app.get('/hola', (req, res) => {
    res.send("<h1>Hola Estudiante</h1><p>El servidor responde. </p>");
})

// Devolviendo datos reales (JSON)
app.get('/contacto', (req, res) => {
    res.json({
        nombre: "Soporte Tecnico",
        email: "ayuda@irsi.com",
        extension: "2205"
    })
})

app.post('/registrar', (req, res) => {
    // Extraemos la info del body
    const infoEstudiante = req.body;

    console.log("Datos recibidos: ", infoEstudiante);
    res.status(201).json({
        mensaje: "Estudiante registrado con exito",
        datos_recibidos: infoEstudiante
    })
})

app.listen(PORT, () => {
    console.log("Servidor activo en el puerto " + PORT);
})