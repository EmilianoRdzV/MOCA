use std::io;

fn main() {
    let mut n = String::new();
    io::stdin().read_line(&mut n).unwrap();

    let numero: i32 = n.trim().parse().unwrap();

    for i in 0..=10 {
        println!("{}", numero * i);
    }
}
