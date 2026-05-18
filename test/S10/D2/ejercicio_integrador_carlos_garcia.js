function obtenerLibrosServidor(callback) {
    console.log('cargando libros...');
    setTimeout(() => {
        const fallo = Math.random() < 0.2;
        if (fallo) {
            return callback(new Error('Fallo en la red'), null);
        }
        const libros = [
            { id: 1, titulo: '100 años de soledad ', disponible: true },
            { id: 2, titulo: 'La Divina Comedia', disponible: true },
            { id: 3, titulo: 'El principito', disponible: true },
            { id: 4, titulo: 'El Quijote', disponible: false },
        ];
        callback(null, libros);
    }, 2000);
}

obtenerLibrosServidor((err, libros) => {
    if (err) {
        return console.log('Error:', err.message);
    }
    console.log(`Llegaron ${libros.length} libros:`);
    libros.forEach((libro) => {
        if (libro.disponible) {
            console.log('-', libro.titulo);
        }
    });
});