fn cross_product(a: (i64, i64), b: (i64, i64)) -> i64 {
    a.0 * b.1 - b.0 * a.1
}

fn distance(a: (i64, i64), b: (i64, i64)) -> f64 {
    (((a.0 - b.0).pow(2) + (a.1 - b.1).pow(2)) as f64).powf(0.5)
}

fn vector(a: (i64, i64), b: (i64, i64)) -> (i64, i64) {
    (b.0 - a.0, b.1 - a.1)
}

#[allow(non_snake_case)]
fn pointsBelong(
    x1: i32,
    y1: i32,
    x2: i32,
    y2: i32,
    x3: i32,
    y3: i32,
    xp: i32,
    yp: i32,
    xq: i32,
    yq: i32,
) -> i32 {
    let a = (x1 as i64, y1 as i64);
    let b = (x2 as i64, y2 as i64);
    let c = (x3 as i64, y3 as i64);
    let p = (xp as i64, yp as i64);
    let q = (xq as i64, yq as i64);

    let ab = distance(a, b);
    let bc = distance(b, c);
    let ca = distance(c, a);
    if (ab + bc <= ca) || (bc + ca <= ab) || (ca + ab <= bc) {
        return 0;
    }

    let pa = vector(p, a);
    let pb = vector(p, b);
    let pc = vector(p, c);
    let cpab = cross_product(pa, pb);
    let cpbc = cross_product(pb, pc);
    let cpca = cross_product(pc, pa);
    let pin = (cpab >= 0 && cpbc >= 0 && cpca >= 0) || (cpab < 0 && cpbc < 0 && cpca < 0);

    let qa = vector(q, a);
    let qb = vector(q, b);
    let qc = vector(q, c);
    let cqab = cross_product(qa, qb);
    let cqbc = cross_product(qb, qc);
    let cqca = cross_product(qc, qa);
    let qin = (cqab >= 0 && cqbc >= 0 && cqca >= 0) || (cqab < 0 && cqbc < 0 && cqca < 0);

    if pin && !qin {
        return 1;
    }

    if !pin && qin {
        return 2;
    }

    if pin && qin {
        return 3;
    }

    return 4;
}
