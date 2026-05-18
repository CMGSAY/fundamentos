const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.post('/login', (req, res) => {

    const { usuario, password } = req.body;

    if (usuario === "admin" && password === "1234") {

        return res.json({
            status: "ok",
            mensaje: "Login exitoso"
        });

    } else {

        return res.status(401).json({
            status: "error",
            mensaje: "Usuario o contraseña incorrectos"
        });

    }

});

app.listen(port, () => {
    console.log(`Servidor escuchando en http://localhost:${port}`);
});