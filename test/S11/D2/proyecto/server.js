const express = require('express');
const path = require('path');
const db = require('./db');

const app = express();
const PORT = 3000;

// mildware de configuracion 
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

app.post('/misiones', (req, res) => {
    const {nombre, destino, rango_peligro, detalles} = req.body;
    
    console.log('[SERVIDOR] Datos recibidos desde la web. Nave ${nombre} hacia  ${destino}', req.body);

    const querySQL = `
        INSERT INTO misiones (nombre, destino, rango_peligro, detalles)
        VALUES (?, ?, ?, ?)`;

    db.query(querySQL, [nombre, destino, rango_peligro, detalles], (err, result) => {
        if (err) {
            console.error('[SERVIDOR] Error al insertar la mision en la base de datos:', err);
           return res.status(500).send('Error al insertar la mision en la base de datos');
        }
        // si la insercion fue exitosa
        console.log('[DB] Registro guardado con esxito. ID de la mision: ${result.insertId}');
        

        res.send(
            `
            <Doctype html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                
                <title>Mision Registrada</title>
            </head>
            <body>
                <h1>Registro guardado con exito. ID de la mision: ${result.insertId}</h1>
                <p> La nave <strong>${nombre}</strong> hacia el sector <strong>${destino}</strong> con un rango de peligro de <strong>${rango_peligro}</strong></p>
                
            </body>
            </html>
            `
        )
})
})

app.get('/misiones', (req, res) => {
   console.log('[SERVIDOR] peticion del GET recicibida. Solicitamos historial de misiones..');

   const querySQL = 'SELECT * FROM misiones ORDER BY id DESC';
   db.query(querySQL, (err, result) => {
       if (err) {
           console.error("Error al consultar la base de datos: ", err)
           return res.status(500).send(<h1> Error critico. No se pudo consultar la base de datos </h1>);
        
       }
       let filasHTML = ''

       resultado.forEach((mision) => {
           filasHTML += `
                <tr>
                    <td>${mision.id}</td>
                    <td>${mision.nombre_nave}</td>
                    <td>${mision.destino}</td>
                    <td>${mision.rango_peligro}</td>
                    <td>${mision.detalles || 'Sin detalles'}</td>
                </tr>
           `
       });

       if (resultado.length === 0) {
           filasHTML = '<h1>No hay misiones registradas</h1>';
       }

       res.send(
           `
            <Doctype html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                
                <title> Bitacora de misiones</title>
            </head>
            <body>
                ${filasHTML}
            </body>
            </html>
            `
       )
       });

app.listen(PORT, () => {
    console.log(`Servidor escuchando en http://localhost:${PORT}`);
});
