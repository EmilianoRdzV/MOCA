use std::io;

fn main() {
    let mut entrada = String::new();
    io::stdin().read_line(&mut entrada).unwrap();
    let area: u64 = entrada.trim().parse().unwrap();

    let mut es_cuadrado = false;
    let mut es_rectangulo = false;

    let lado = (area as f64).sqrt().round() as u64;
    if lado * lado == area && lado > 1 {
        es_cuadrado = true;
    }

    let limite = (area as f64).sqrt() as u64;
    for i in 2..=limite {
        if area % i == 0 && i * i != area {
            es_rectangulo = true;
            break;
        }
    }

    if es_cuadrado && es_rectangulo {
        println!("ambos");
    } else if es_cuadrado {
        println!("cuadrado");
    } else if es_rectangulo {
        println!("rectangulo");
    } else {
        println!("ninguno");
    }
}
