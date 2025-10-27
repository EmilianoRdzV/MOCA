use std::io::{self, Read, Write};

fn main() {
    let mut a_str = String::new();
    io::stdin().read_line(&mut a_str).unwrap();
    let a: f64 = a_str.trim().parse().unwrap();

    let mut b_str = String::new();
    io::stdin().read_line(&mut b_str).unwrap();
    let b: f64 = b_str.trim().parse().unwrap();

    let c = ((a * a) + (b * b)).sqrt();
    let salida = format!("{:.3f}", c);

    io::stdout().write_all(salida.as_bytes()).unwrap();
}
