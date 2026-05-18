const express = require('express');
const app = express();
const PORT = 4000;

app.get('/buscar', (req, res) => {
    const nombre = req.query.nombre;
    const rol = req.query.rol;

    if (!nombre) {
        return res.status(400).json({ error: "Faltan parámetros 'nombre'" });
    }

    if (!rol) {
        return res.status(400).json({ error: "Faltan parámetros 'rol'" });
    }

    res.json({mensaje: `Se ha encontrado a ${rol} ${nombre} en la base de datos.`});

});

app.listen(PORT, () => {
    console.log(`Servidor escuchando en http://localhost:${PORT}`);
});