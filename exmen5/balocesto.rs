use std::io::{self, BufRead};   

fn main(){

    let mut a = String::new();
    io::stdin().read_line(&mut a).unwrap();

    let altura: f32 = a.trim().parse().unwrap();


    if altura >= 1.70{
        println!("Aceptado");
    } else {
        println!("Rechazado");
    }

}