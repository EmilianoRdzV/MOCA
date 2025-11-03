use std::io::{self, Read};
use std::collections::VecDeque; // Importar la cola
use std::fmt::Write; // Para escribir en el string de salida

fn main() {
    // Leer toda la entrada de golpe
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    
    // Iterador para leer la entrada palabra por palabra
    let mut iter = buf.split_whitespace();
    
    // Leer N
    let n: i32 = iter.next().unwrap().parse().unwrap();
    
    let mut fila: VecDeque<i64> = VecDeque::new();
    let mut totalTacosVendidos: i64 = 0;
    
    // String para construir la salida
    let mut salida = String::new();
    
    for _ in 0..n {
        let op: i32 = iter.next().unwrap().parse().unwrap();
        
        match op {
            1 => {
                // (Push) Leer el siguiente número y añadirlo al final
                let t: i64 = iter.next().unwrap().parse().unwrap();
                fila.push_back(t);
            },
            2 => {
                // (Pop) Quitar del frente
                if let Some(tacos) = fila.pop_front() {
                    totalTacosVendidos += tacos;
                }
            },
            3 => {
                // (Size) Escribir el tamaño en el buffer de salida
                writeln!(&mut salida, "{}", fila.len()).unwrap();
            },
            4 => {
                // Escribir el total en el buffer de salida
                writeln!(&mut salida, "{}", totalTacosVendidos).unwrap();
            },
            _ => {
                // Caso por defecto (no debería pasar)
            }
        }
    }
    
    print!("{}", salida);
}