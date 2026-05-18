const express = require('express');
const app = express();
const PORT = 4000;
app.use(express.json());

T
app.post('/despacho', (req, res) => {

    const { recurso, peso } = req.body;

    setTimeout(() => {

        console.log(`[LOG] Recibido pedido de ${recurso} (${peso}kg).`);

        
        if (peso > 500) {

            console.log("Estado: RECHAZADO.");

            return res.status(400).json({
                ok: false,
                mensaje: "Capacidad de hangar excedida"
            });
        }

        console.log("Estado: ACEPTADO.");

        
        res.json({
            ok: true,
            mensaje: "Despacho programado",
            id: "A-102"
        });

    }, 1500);

});

app.listen(PORT, () => {
    console.log("Servidor activo en el puerto " + PORT);
})