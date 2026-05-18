// validador.js

// Captura de argumentos desde la terminal
const piloto = process.argv[2];
const carga = Number(process.argv[3]);
const capacidad = Number(process.argv[4]);

// Validación de entradas
if (!piloto || isNaN(carga) || isNaN(capacidad)) {
  console.error("Error: argumentos inválidos. Uso: node validador.js <piloto> <carga> <capacidad>");
  process.exit(1);
}

// Función arrow para calcular porcentaje
const calcularPorcentaje = (carga, capacidad) => (carga / capacidad) * 100;

// Determinar estado con operador ternario
const porcentaje = calcularPorcentaje(carga, capacidad);
const estado = porcentaje > 90 ? "Peligro" : "Seguro";

// Crear objeto reporte
const reporte = {
  piloto,
  carga,
  capacidad,
  porcentaje: Math.round(porcentaje),
  estado
};

// Salida en consola
console.log(`Analizando despacho para: ${piloto} ...`);
console.log(reporte);

if (estado === "Peligro") {
  console.log("¡ALERTA! : Peso excedido, despegue abortado.");
}
