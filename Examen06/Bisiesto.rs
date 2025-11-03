use std::io;

fn main() {
    let mut entrada = String::new();
    io::stdin().read_line(&mut entrada).unwrap();

    let año: i32 = entrada.trim().parse().unwrap();

    if año % 400 == 0 {
        println!("ES BISIESTO");
    } else if año % 100 == 0 {
        println!("NO ES BISIESTO");
    } else if año % 4 == 0 {
        println!("ES BISIESTO");
    } else {
        println!("NO ES BISIESTO");
    }
}
