use std::io::{stdin, BufRead};

fn main() {
    println!("{expected}", expected = stdin().lock().lines().next().unwrap().unwrap());
}
