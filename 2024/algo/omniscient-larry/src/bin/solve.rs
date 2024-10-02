use omniscient_larry::omniscient_god::solve;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    use std::io::{self, BufRead};

    let mut stdin = io::stdin().lock();

    let mut line = String::new();
    stdin.read_line(&mut line)?;

    for _ in 0..line.trim().parse::<u32>()? {
        line.clear();
        stdin.read_line(&mut line)?;

        println!("{}", solve(line.trim()));
    }

    line.clear();
    stdin.read_line(&mut line)?;
    eprint!("{line}");

    Ok(())
}
