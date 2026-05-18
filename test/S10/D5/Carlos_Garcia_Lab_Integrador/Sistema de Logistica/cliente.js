const recurso = process.argv[2];
const peso = Number(process.argv[3]);


if (!recurso || !peso) {

    console.log("Uso correcto:");
    console.log('node cliente.js "Oxigeno" 350');

    process.exit();
}


function prepararPaquete(nombre, peso, callback) {

    
    (() => {
        console.log(`Empacando ${nombre}...`);
    })();

    callback(nombre, peso);
}


prepararPaquete(recurso, peso, async (nombre, peso) => {

    console.log("Enviando datos al servidor central...");

    
    const paquete = {
        recurso: nombre,
        peso: peso
    };

    try {

        const respuesta = await fetch('http://localhost:4000/despacho', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(paquete)
        });

        const datos = await respuesta.json();

        console.log("Respuesta del servidor:");
        console.log(datos);

    } catch (error) {

        console.log("Error al conectar con el servidor");
        console.log(error.message);

    }

});