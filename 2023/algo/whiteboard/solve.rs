//! Main idea: Note that obviously all numbers on the whiteboard can be written of the form `33a + 8b`
//! since our new number is always a linear combination of other numbers.
//!
//! We can also show using induction that `a + b = 1`, so all numbers on the whiteboard can be written
//! of the form `33a + 8(1 - a) = 25a + 8`. Let `f(a) = 25a + 8`.
//!
//! Initially we have `33 = f(1)` and `8 = f(0)` written on the whiteboard.
//!
//! For convenience, write `f(-1) = 2f(0) - f(1)`.
//! Note that if we have `f(a)`, we can write `2f(a) - f(0) = f(2a)` and `2f(a) - f(-1) = f(2a + 1)` on the whiteboard.
//! Thus, to write `x = f(a)` on the whiteboard, we can write `x` incrementally using `a`'s binary representation.
//!
//! To run this code, add the following to your `Cargo.toml` or use [rust-script](https://rust-script.org/).
//!
//! ```cargo
//! [dependencies]
//! rug = "1.15.0"
//! ```

use rug::Integer;
use std::io;

fn read_line() -> String {
    eprintln!("TRY READ");
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("io error");
    // strip trailing new lines
    s.truncate(s.trim_end_matches(['\r', '\n']).len());
    eprintln!("READ: {s}");
    s
}

fn assert_read_line(s: &str) {
    let line = read_line();
    assert_eq!(line, s);
}

fn f(a: Integer) -> Integer {
    25 * a + 8
}

fn query_combine(a1: Integer, a2: Integer) {
    println!("{} {}", f(a1), f(a2));
}

fn solve_testcase() {
    let goal: Integer = {
        let line = read_line();

        let (pref, goal) = line.split_at("Goal: ".len());
        assert_eq!(pref, "Goal: ");

        let goal = goal.parse::<Integer>().expect("goal is not an integer");
        assert_eq!(goal.clone() % 25, 8);
        (goal - 8) / 25
    };

    // stO HBD BRYAN GAO Orz
    assert_read_line("{8, 33}");

    // make -1
    query_combine(0.into(), 1.into());

    let mut current: Integer = 1.into();

    for c in goal.to_string_radix(2).chars().skip(1) {
        match c {
            '0' => {
                query_combine(current.clone(), 0.into());
                current *= 2;
            }
            '1' => {
                query_combine(current.clone(), (-1).into());
                current = current * 2 + 1
            }
            _ => unreachable!()
        }
    }

    assert_eq!(current, goal);

    let line = read_line();
    assert!(line.ends_with("Good job"));
}

fn main() {
    for _ in 0..5 {
        solve_testcase();
    }

    assert_read_line("happy birthday to you too!");
    eprintln!("FLAG: {}", read_line());
}
