use std::io;

fn main() {
    let mut linea = String::new();
    io::stdin().read_line(&mut linea).unwrap();
    
    let mut palabras = linea.split_whitespace();
    
    let numH: i32 = palabras.next().unwrap().parse().unwrap();
    let pesoH: i32 = palabras.next().unwrap().parse().unwrap();
    let numE: i32 = palabras.next().unwrap().parse().unwrap();
    let pesoE: i32 = palabras.next().unwrap().parse().unwrap();
    
    let pesoTotal = (numH * pesoH) + (numE * pesoE);
    
    println!("{}", pesoTotal);
}