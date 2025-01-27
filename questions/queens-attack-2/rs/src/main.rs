use std::collections::HashSet;
use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'queensAttack' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. INTEGER r_q
 *  4. INTEGER c_q
 *  5. 2D_INTEGER_ARRAY obstacles
 */

fn count(n: &i32, p: &(i32, i32), d: &(i32, i32), obstacles: &HashSet<(i32, i32)>) -> i32 {
    let (rd, cd) = d;
    let (rp, cp) = p;
    let (nr, nc) = (rd + rp, cd + cp);
    if nr < 1 || nr > *n || nc < 1 || nc > *n {
        return 0
    }

    let np = (nr, nc);
    if obstacles.contains(&np) {
        return 0
    }

    count(n, &np, d, obstacles) + 1
}

#[allow(non_snake_case, unused_variables)]
fn queensAttack(n: i32, k: i32, r_q: i32, c_q: i32, obstacles: &[Vec<i32>]) -> i32 {
    let ds: Vec<(i32, i32)> = vec![
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ];
    let os = obstacles.iter().map(|o| (o[0], o[1])).collect();
    let p = (r_q, c_q);
    ds.iter().map(|d| count(&n, &p, d, &os)).sum()
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let first_multiple_input: Vec<String> = stdin_iterator.next().unwrap().unwrap()
        .split(' ')
        .map(|s| s.to_string())
        .collect();

    let n = first_multiple_input[0].trim().parse::<i32>().unwrap();

    let k = first_multiple_input[1].trim().parse::<i32>().unwrap();

    let second_multiple_input: Vec<String> = stdin_iterator.next().unwrap().unwrap()
        .split(' ')
        .map(|s| s.to_string())
        .collect();

    let r_q = second_multiple_input[0].trim().parse::<i32>().unwrap();

    let c_q = second_multiple_input[1].trim().parse::<i32>().unwrap();

    let mut obstacles: Vec<Vec<i32>> = Vec::with_capacity(k as usize);

    for i in 0..k as usize {
        obstacles.push(Vec::with_capacity(2_usize));

        obstacles[i] = stdin_iterator.next().unwrap().unwrap()
            .trim_end()
            .split(' ')
            .map(|s| s.to_string().parse::<i32>().unwrap())
            .collect();
    }

    let result = queensAttack(n, k, r_q, c_q, &obstacles);

    writeln!(&mut fptr, "{}", result).ok();
}
