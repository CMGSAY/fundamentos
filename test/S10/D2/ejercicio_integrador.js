const express = require('express')
const app = express()
const PORT = 3000
app.use(express.json());

// Logica del motor
function procesarEstudinates(lista, callback) {
    if (!Array.isArray(lista) || lista.length === 0) {
        return callback("Error: La lista de estudiantes debe ser un array no vacio.");
 
    }

    const aprobados = [];
    const reprobados = [];

    lista.forEach(estudiante => {
        if (estudiante.nota >= 70) {
            aprobados.push(estudiante.nombre);
        } else {
            reprobados.push(estudiante.nombre);
        }
    });

    const reporte = {
        aprobados,
        reprobados
    };

    return callback(null, reporte);

}

app.post('/analizar-clase', (req, res) => {
    const { estudiantes } = req.body;

    procesarEstudinates(estudiantes, (error, reporte) => {
        if (error) {
            res.status(400).json({
                ok: false,
                mensaje: error });
        } else {
            res.json(
                {"status": "success",
                "reporte": reporte});
        }
    });
})

app.listen(PORT, () => {
    console.log("Servidor esta activo el puerto" + PORT);
});

