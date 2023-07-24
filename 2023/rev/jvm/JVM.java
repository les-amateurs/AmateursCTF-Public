import java.io.*;

public class JVM {
    static byte[] program;

    public static void main(String[] args) throws IOException {
        File file = new File(args[0]);
        FileInputStream fis = new FileInputStream(file);
        program = new byte[(int) file.length()];
        fis.read(program);
        fis.close();
        vm();
    }

    private static void vm() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int pc = 0;
        int sp = 0;
        int[] stack = new int[1024];
        int[] regs = new int[4];
        byte arg0, arg1, arg2;

        while (pc < program.length) {
            // System.out.println("pc: " + pc);
            // System.out.println("sp: " + sp);
            // System.out.println("regs: " + Arrays.toString(regs));
            // System.out.println("inst: " + (int) program[pc]);
            switch (program[pc]) {
                case 0:
                case 1:
                case 2:
                case 3:
                    arg1 = program[pc];
                    arg2 = program[pc + 1];
                    int tmp = regs[arg1];
                    regs[arg1] = regs[arg2];
                    regs[arg2] = tmp;
                    pc += 2;
                    break;
                case 8:
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    regs[arg1] += arg2;
                    pc += 3;
                    break;
                case 9:
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    regs[arg1] += regs[arg2];
                    pc += 3;
                    break;
                case 12:
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    regs[arg1] -= arg2;
                    pc += 3;
                    break;
                case 13:
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    regs[arg1] -= regs[arg2];
                    pc += 3;
                    break;
                case 16:
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    regs[arg1] *= arg2;
                    pc += 3;
                    break;
                case 17:
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    regs[arg1] *= regs[arg2];
                    pc += 3;
                    break;
                case 20:
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    regs[arg1] /= arg2;
                    pc += 3;
                    break;
                case 21:
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    regs[arg1] /= regs[arg2];
                    pc += 3;
                    break;
                case 24:
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    regs[arg1] %= arg2;
                    pc += 3;
                    break;
                case 25:
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    regs[arg1] %= regs[arg2];
                    pc += 3;
                    break;
                case 28:
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    regs[arg1] <<= arg2;
                    pc += 3;
                    break;
                case 29:
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    regs[arg1] <<= regs[arg2];
                    pc += 3;
                    break;
                case 31:
                    arg1 = program[pc + 1];
                    regs[arg1] = br.read();
                    pc += 2;
                    break;
                case 32:
                    stack[sp++] = br.read();
                    pc++;
                    break;
                case 33:
                    arg1 = program[pc + 1];
                    System.out.print((char) regs[arg1]);
                    pc += 2;
                    break;
                case 34:
                    System.out.print((char) stack[--sp]);
                    pc++;
                    break;
                case 41:
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    if (regs[arg1] == 0)
                        pc = arg2;
                    else
                        pc += 3;
                    break;
                case 42:
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    if (regs[arg1] != 0)
                        pc = arg2;
                    else
                        pc += 3;
                    break;
                case 43:
                    arg1 = program[pc + 1];
                    pc = arg1;
                    break;
                case 52:
                    arg1 = program[pc + 1];
                    stack[sp++] = regs[arg1];
                    pc += 2;
                    break;
                case 53:
                    arg1 = program[pc + 1];
                    regs[arg1] = stack[--sp];
                    pc += 2;
                    break;
                case 54:
                    arg1 = program[pc + 1];
                    stack[sp++] = arg1;
                    pc += 2;
                    break;

                case 127:
                    br.close();
                    return;

                default:
                    arg0 = program[pc];
                    arg1 = program[pc + 1];
                    arg2 = program[pc + 2];
                    program[pc] = (byte) (program[pc] ^ arg1 ^ arg2);
                    program[pc + 1] = (byte) (program[pc] ^ arg0 ^ arg2);
                    program[pc + 2] = (byte) (program[pc + 1] ^ arg0 ^ arg1);
                    break;
            }
        }
    }
}