const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.static('public'));

app.post('/evaluar-credito', (req, res) => {
    const { nombre, ingresos, montoSolicitado } = req.body;
    const credito = evaluarCredito(ingresos, montoSolicitado);
    res.render('resultado', { nombre, credito });
});

app.listen(PORT, () => {
    console.log("Servidor esta activo el puerto" + PORT);
});