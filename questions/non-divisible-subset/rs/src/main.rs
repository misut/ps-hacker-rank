use std::collections::HashMap;
use std::{cmp, env};
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'nonDivisibleSubset' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY s
 */

#[allow(non_snake_case)]
fn nonDivisibleSubset(k: i32, s: &[i32]) -> i32 {
    let mut ks = HashMap::new();
    for n in s {
        ks.entry(n % k).and_modify(|c| *c += 1).or_insert(1);
    }

    let has_half = ks.contains_key(&(k / 2));
    let has_zero = ks.contains_key(&0);
    let is_even = k % 2 == 0;
    let mut result = has_zero as i32 + if is_even { has_half as i32 } else { 0 };
    for n in 1..(k / 2 + 1 - is_even as i32) {
        result += cmp::max(ks.get(&n), ks.get(&(k - n))).unwrap_or(&0);
    }
    result
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

    let s: Vec<i32> = stdin_iterator.next().unwrap().unwrap()
        .trim_end()
        .split(' ')
        .map(|s| s.to_string().parse::<i32>().unwrap())
        .collect();

    let result = nonDivisibleSubset(k, &s);

    writeln!(&mut fptr, "{}", result).ok();
}
