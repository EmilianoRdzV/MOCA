use std::io::{self, Read};

fn main() {
    let mut entrada = String::new();
    io::stdin().read_to_string(&mut entrada).unwrap();
    let mut iter = entrada.split_whitespace();

    let num_digitos: usize = iter.next().unwrap().parse().unwrap();
    let digitos: Vec<i32> = iter.take(num_digitos).map(|s| s.parse().unwrap()).collect();

    let mitad = num_digitos / 2;
    let suma_uno: i32 = digitos[..mitad].iter().sum();
    let suma_dos: i32 = digitos[mitad..].iter().sum();

    if suma_uno == suma_dos {
        println!("{} 1", suma_uno);
    } else {
        println!("{} 0", suma_uno + suma_dos);
    }
}
