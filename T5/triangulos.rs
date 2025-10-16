use std::io;

fn main() {
    let mut linea = String::new();
    io::stdin().read_line(&mut linea).expect("Error al leer la línea");

    // Creamos un vector (lista) de números a partir de la línea leída
    let numeros: Vec<i32> = linea
        .split_whitespace() // 1. Divide el texto por los espacios
        .map(|s| s.parse().expect("No es un número")) // 2. Convierte cada parte a número
        .collect(); // 3. Junta los resultados en el vector

    // Asignamos los valores para mayor claridad
    let ancho = numeros[0];
    let largo = numeros[1];
    let alto = numeros[2];

    let volumen = ancho * largo * alto;

    println!("{}", volumen);
}