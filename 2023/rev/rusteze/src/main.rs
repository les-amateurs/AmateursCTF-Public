use std::io::Write;

fn main() {
    print!("> ");
    std::io::stdout().flush().unwrap();

    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    let input = line.trim().as_bytes();

    if input.len() != 38 {
        println!("Wrong!");
        return;
    }

    let stuff: [u8; 38] = [39, 151, 87, 225, 169, 117, 102, 62, 27, 99, 227, 160, 5, 115, 89, 251, 10, 67, 143, 224, 186, 192, 84, 153, 6, 191, 159, 47, 196, 170, 166, 116, 30, 221, 151, 34, 237, 197];

    let mut test: [u8; 38] = [0; 38];
    let mut i = 0;
    while i < 38 {
        let mut c: u8 = input[i] ^ stuff[i];
        c = c.rotate_left(2);
        test[i] = c;
        i += 1;
    }

    let okay: [u8; 38] = [25, 235, 216, 86, 51, 0, 80, 53, 97, 220, 150, 111, 181, 13, 164, 122, 85, 232, 254, 86, 151, 222, 157, 175, 212, 71, 175, 193, 194, 106, 90, 172, 177, 162, 138, 89, 82, 226];
    i = 0;
    while i < 38 {
        if test[i] != okay[i] {
            println!("Wrong!");
            return;
        }
        i += 1;
    }

    println!("Correct!");
}
