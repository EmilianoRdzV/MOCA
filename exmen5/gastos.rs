use std::io;

fn main() {
    let mut linea = String::new();
    io::stdin().read_line(&mut linea).unwrap();

    let mut total = 0;
    let mut cantidad = 0;

    for gasto in linea.trim().split_whitespace() {
        let valor: i32 = gasto.parse().unwrap();
        if valor == 0 {
            break;
    }
        total += valor;
        cantidad += 1;
    }

    println!("{} {}", total, cantidad);
}
