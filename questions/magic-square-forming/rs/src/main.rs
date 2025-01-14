use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'formingMagicSquare' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY s as parameter.
 */

fn rotate(s: &[Vec<i32>], n: usize) -> Vec<Vec<i32>> {
    let mut rotated = vec![vec![0; n]; n];
    for i in 0..n {
        for j in 0..n {
            rotated[j][n - i - 1] = s[i][j];
        }
    }
    rotated
}

fn transpose(s: &[Vec<i32>], n: usize) -> Vec<Vec<i32>> {
    let mut transposed = vec![vec![0; n]; n];
    for i in 0..n {
        for j in 0..n {
            transposed[j][i] = s[i][j];
        }
    }
    transposed
}

fn cost(d: &[Vec<i32>], s: &[Vec<i32>]) -> i32 {
    let mut c = 0;
    for i in 0..3 {
        for j in 0..3 {
            c += (d[i][j] - s[i][j]).abs();
        }
    }
    c
}

#[allow(non_snake_case)]
fn formingMagicSquare(s: &[Vec<i32>]) -> i32 {
    let magic_square = vec![vec![8, 3, 4], vec![1, 5, 9], vec![6, 7, 2]];
    let magic_squares = vec![
        magic_square.clone(),
        rotate(&magic_square, 3),
        rotate(&rotate(&magic_square, 3), 3),
        rotate(&rotate(&rotate(&magic_square, 3), 3), 3),
        transpose(&magic_square, 3),
        rotate(&transpose(&magic_square, 3), 3),
        rotate(&rotate(&transpose(&magic_square, 3), 3), 3),
        rotate(&rotate(&rotate(&transpose(&magic_square, 3), 3), 3), 3),
    ];
    magic_squares.iter().map(|d| cost(d, s)).min().unwrap()
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let mut s: Vec<Vec<i32>> = Vec::with_capacity(3_usize);

    for i in 0..3_usize {
        s.push(Vec::with_capacity(3_usize));

        s[i] = stdin_iterator
            .next()
            .unwrap()
            .unwrap()
            .trim_end()
            .split(' ')
            .map(|s| s.to_string().parse::<i32>().unwrap())
            .collect();
    }

    let result = formingMagicSquare(&s);

    writeln!(&mut fptr, "{}", result).ok();
}
