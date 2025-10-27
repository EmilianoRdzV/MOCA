use std::io;

fn main() {
    let mut linea_a = String::new();
    io::stdin().read_line(&mut linea_a).unwrap();
    let lado_a: f64 = linea_a.trim().parse().unwrap();

    let mut linea_b = String::new();
    io::stdin().read_line(&mut linea_b).unwrap();
    let lado_b: f64 = linea_b.trim().parse().unwrap();

    let hipotenusa = (lado_a.powi(2) + lado_b.powi(2)).sqrt();
    println!("{:.3}", hipotenusa);
}
