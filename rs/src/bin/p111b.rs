use itertools::Itertools;
use primal::is_prime;

// Get `n`-digit number with `free_digits` at given indices and `d`s elsewhere
// Ex: build_number(4, 1, [5, 6], [0, 2]) => 5161
fn build_number(
    n: usize,
    d: usize,
    free_digits: &Vec<usize>,
    free_digit_indices: &Vec<usize>,
) -> Option<usize> {
    let mut digits = vec![d; n];
    for i in 0..free_digits.len() {
        digits[free_digit_indices[i]] = free_digits[i];
    }
    if digits[0] == 0 {
        // Not an n-digit number
        None
    } else {
        let number = digits.iter().fold(0, |n, d| n * 10 + d);
        Some(number)
    }
}

// Get all `n`-digit integers with `k` occurrences of digit `d`.
fn n_digit_numbers_with_k_ds(n: usize, k: usize, d: usize) -> Vec<usize> {
    let n_free_digits = n - k;
    let non_d_digits = (0..10).filter(|x| *x != d);
    // Get all `n_free_digits`-tuples of non-`d` digits
    let free_digits_choices = vec![non_d_digits; n_free_digits]
        .into_iter()
        .multi_cartesian_product();
    // Order matters in free digits (e.g. we have both [1, 2] and [2, 1]), so order-independent
    // combinations of indices suffice to construct all integers
    let free_digit_indices_choices = (0..n).combinations(n_free_digits);

    let mut numbers = Vec::new();
    for free_digits in free_digits_choices {
        for free_digit_indices in free_digit_indices_choices.clone() {
            match build_number(n, d, &free_digits, &free_digit_indices) {
                Some(n) => numbers.push(n),
                None => (),
            }
        }
    }
    numbers
}

fn s(n: usize, d: usize) -> usize {
    // Consider first `n`-digit primes with `n` `d`s, then `n-1` `d`s, etc. We can stop as soon as
    // we find a nonempty set.
    for k in (0..n + 1).rev() {
        let mut n_digit_primes_with_k_ds = n_digit_numbers_with_k_ds(n, k, d)
            .into_iter()
            .filter(|p| is_prime(*p as u64))
            .peekable();
        if n_digit_primes_with_k_ds.peek().is_some() {
            return n_digit_primes_with_k_ds.sum::<usize>();
        }
    }
    panic!();
}

fn main() {
    let n = 10;
    println!("{}", (0..10).map(|d| s(n, d)).sum::<usize>());
}
