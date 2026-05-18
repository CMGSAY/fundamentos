const express = require("express");
const app = express();
const PORT = 3000;
app.use(express.json());


function procesarEstudiantes(lista, callback) {

    // Validar si es arreglo y si no está vacío
    if (!Array.isArray(lista) || lista.length === 0) {
        return callback("Error: la lista está vacía o no es un arreglo", null);
    }

    const aprobados = [];
    const reprobados = [];

    // Clasificar estudiantes
    lista.forEach((estudiante) => {

        if (estudiante.nota >= 70) {
            aprobados.push(estudiante.nombre);
        } else {
            reprobados.push(estudiante.nombre);
        }

    });

    // Resultado final
    const reporte = {
        total: lista.length,
        aprobados,
        reprobados
    };

    callback(null, reporte);
}

// Ruta POST
app.post("/analizar-clase", (req, res) => {

    const { estudiantes } = req.body;

    procesarEstudiantes(estudiantes, (error, resultado) => {

        if (error) {
            return res.status(400).json({
                "estatus": "error",
                mensaje: error
            });
        }

        res.json({
            "estatus": "success",
            reporte: resultado
        });

    });

});

app.listen(PORT, () => {
    console.log("Servidor activo en el puerto " + PORT);
})