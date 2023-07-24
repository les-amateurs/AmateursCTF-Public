use std::io::Write;

static mut item: [u8; 30] = [192, 167, 229, 183, 3, 70, 53, 38, 174, 26, 55, 212, 152, 218, 57, 23, 136, 227, 125, 143, 242, 174, 25, 73, 14, 220, 233, 54, 130, 95];

fn enc(input: &[u8]) -> Vec<u8> {
    let stuff: [u8; 35] = [210, 165, 246, 177, 31, 108, 51, 61, 132, 61, 46, 198, 143, 132, 35, 123, 163, 191, 118, 180, 203, 166, 29, 124, 36, 219, 245, 108, 149, 125, 86, 97, 133, 77, 47];

    let mut output: Vec<u8> = Vec::new();
    for i in 0..input.len() {
        let mut c: u8 = input[i] ^ stuff[i];
        unsafe {
            if i < 30 {
                item[i] ^= c;
            }
        }
        c = c.rotate_left(2);
        output.push(c);
    }
    output
}

fn main() {
    print!("> ");
    std::io::stdout().flush().unwrap();

    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    let input = line.trim().as_bytes();

    if input.len() != 35 {
        println!("Wrong!");
        return;
    }

    let test = enc(input);
    let okay: [u8; 35] = [134, 43, 18, 15, 153, 204, 29, 85, 183, 57, 197, 190, 243, 171, 93, 144, 95, 95, 76, 175, 182, 43, 241, 108, 237, 190, 118, 20, 155, 136, 136, 32, 163, 160, 4];
    if test != okay {
        println!("Wrong!");
        return;
    }

    println!("Correct!");
    // unsafe {
    //     println!(
    //         "The flag is: {}",
    //         String::from_utf8_lossy(&item).to_string()
    //     );
    // }
}
