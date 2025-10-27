use std::io;

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).unwrap();
    let n: usize = n_str.trim().parse().unwrap();

    let mut sumas_columnas = vec![0; n];

    for _ in 0..n {
        let mut fila_str = String::new();
        io::stdin().read_line(&mut fila_str).unwrap();
        let fila: Vec<i32> = fila_str
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();

        for j in 0..n {
            sumas_columnas[j] += fila[j];
        }
    }

    let salida = sumas_columnas
        .iter()
        .map(|x| x.to_string())
        .collect::<Vec<_>>()
        .join(" ");

    print!("{}", salida);
}
 