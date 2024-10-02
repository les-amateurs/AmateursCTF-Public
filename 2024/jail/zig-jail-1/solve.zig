comptime {
    _ = @cImport({
        @cUndef("H\n#include </app/flag.txt> //");
    });
}
