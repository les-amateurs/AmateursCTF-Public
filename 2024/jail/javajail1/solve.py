text = '''import java.util.Scanner;
import java.io.*;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("flag.txt");
        Scanner sc = new Scanner(file);
        System.out.println(sc.nextLine());
    }
}'''

out = ''
for c in text:
    out += f'\\u{ord(c):04x}'
print(out + '\n--EOF--')