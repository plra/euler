use primal::{self, Sieve};

fn digit_counts(mut p: usize) -> [usize; 10] {
    let mut counts = [0; 10];
    while p > 0 {
        let d = p % 10;
        counts[d] += 1;
        p /= 10;
    }
    counts
}

fn sigma(sieve: &Sieve, n: u32) -> usize {
    let mut max_digit_counts = [0; 10];
    let mut ss = [0; 10];

    let min_p = usize::pow(10, n - 1);
    for p in sieve.primes_from(min_p).take_while(|x| *x < 10 * min_p) {
        let counts = digit_counts(p);
        for d in 0..10 {
            if counts[d] > max_digit_counts[d] {
                // We have a new max repeat digit count; reset count and sum
                max_digit_counts[d] = counts[d];
                ss[d] = p;
            } else if counts[d] == max_digit_counts[d] {
                ss[d] += p;
            }
        }
    }
    ss.iter().sum()
}

fn main() {
    let n = 4;

    let sieve = Sieve::new(usize::pow(10, n));
    // let (m, n, s) = m_n_s(&sieve, n);
    // println!("M={:?}, N={:?}, S={:?}", m, n, s);
    println!("{}", sigma(&sieve, n));
}
