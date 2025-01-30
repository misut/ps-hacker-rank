use std::collections::HashMap;
use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'organizingContainers' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts 2D_INTEGER_ARRAY container as parameter.
 */

#[allow(non_snake_case)]
fn organizingContainers(container: &[Vec<i32>]) -> String {
    let csum = container.iter().map(|c| c.iter().sum()).fold(HashMap::new(), |mut map, sum: i32| {
        map.entry(sum).and_modify(|v| *v += 1).or_insert(1);
        map
    });
    let n = container.len();
    let bsum = (0..n).into_iter().map(|i| container.iter().map(|c| c[i]).sum()).fold(HashMap::new(), |mut map, sum| {
        map.entry(sum).and_modify(|v| *v += 1).or_insert(1);
        map
    });
    String::from(if csum == bsum {
        "Possible"
    } else {
        "Impossible"
    })
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let q = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    for _ in 0..q {
        let n = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

        let mut container: Vec<Vec<i32>> = Vec::with_capacity(n as usize);

        for i in 0..n as usize {
            container.push(Vec::with_capacity(n as usize));

            container[i] = stdin_iterator.next().unwrap().unwrap()
                .trim_end()
                .split(' ')
                .map(|s| s.to_string().parse::<i32>().unwrap())
                .collect();
        }

        let result = organizingContainers(&container);

        writeln!(&mut fptr, "{}", result).ok();
    }
}
