use std::io;

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).unwrap();
    let n: i32 = n_str.trim().parse().unwrap();

    let mut m_str = String::new();
    io::stdin().read_line(&mut m_str).unwrap();
    let m: i32 = m_str.trim().parse().unwrap();

    let gil = (n / m) + (n % m);
    println!("{}", gil);
}
