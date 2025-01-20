use std::env;
use std::fs::File;
use std::i32::MIN;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'climbingLeaderboard' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY ranked
 *  2. INTEGER_ARRAY player
 */

#[allow(non_snake_case)]
fn climbingLeaderboard(ranked: &[i32], player: &[i32]) -> Vec<i32> {
    let mut deduped_ranked = ranked.to_vec();
    deduped_ranked.dedup();

    let mut current_rank = 0;
    player
        .into_iter()
        .rev()
        .map(|score| {
            while score < &deduped_ranked.get(current_rank).unwrap_or(&MIN) {
                current_rank += 1;
            }
            current_rank as i32 + 1
        })
        .collect::<Vec<i32>>()
        .into_iter()
        .rev()
        .collect()
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let _ranked_count = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim()
        .parse::<i32>()
        .unwrap();

    let ranked: Vec<i32> = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim_end()
        .split(' ')
        .map(|s| s.to_string().parse::<i32>().unwrap())
        .collect();

    let _player_count = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim()
        .parse::<i32>()
        .unwrap();

    let player: Vec<i32> = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim_end()
        .split(' ')
        .map(|s| s.to_string().parse::<i32>().unwrap())
        .collect();

    let result = climbingLeaderboard(&ranked, &player);

    for i in 0..result.len() {
        write!(&mut fptr, "{}", result[i]).ok();

        if i != result.len() - 1 {
            writeln!(&mut fptr).ok();
        }
    }

    writeln!(&mut fptr).ok();
}
