use std::io::{self, Read, Write};

fn main() {
    // 1. Leer toda la entrada de golpe
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    
    // 2. Procesar la entrada y formatear la salida en una cadena
    // .trim()       -> Quita saltos de línea/espacios al inicio y final
    // .split_whitespace() -> Crea un iterador de "palabras" (bits)
    // .map(...)     -> Transforma cada "bit" (si es "1" -> "0", si no -> "1")
    // .collect()    -> Reúne los bits transformados en un vector
    // .join(" ")    -> Une el vector con espacios
    let salida: String = buf.trim()
        .split_whitespace()
        .map(|bit| if bit == "1" { "0" } else { "1" })
        .collect::<Vec<&str>>()
        .join(" ");
        
    // 3. Escribir la salida final sin salto de línea extra
    io::stdout().write_all(salida.as_bytes()).unwrap();
}