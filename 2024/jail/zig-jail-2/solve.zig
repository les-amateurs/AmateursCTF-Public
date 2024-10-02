const std = @import("std");

const Loop = struct {
    pub fn UnalignedLoop(comptime arg: anytype, comptime item: fn (comptime @TypeOf(arg)) u8, comptime count: u64) u8 {
        const half = count / 2;
        const lower = std.mem.alignBackward(u64, half, 1 << (63 -| @clz(half)));
        return struct {
            pub const unwrap = switch (count) {
                0 => 0,
                1 => item(arg),
                else => AlignedLoop(arg, item, lower) + UnalignedLoop(arg, item, count - lower),
            };
        }.unwrap;
    }

    fn AlignedLoop(comptime arg: anytype, comptime item: fn (comptime @TypeOf(arg)) u8, comptime count: u64) u8 {
        return struct {
            pub const unwrap = switch (count) {
                0 => 0,
                1 => item(arg),
                else => // if (@popCount(count) != 1)
                //     UnalignedLoop(arg, item, count)
                // else
                AlignedLoop(arg, item, count / 2) + AlignedLoop(arg, item, count / 2),
            };
        }.unwrap;
    }
}.UnalignedLoop;

const Arg = struct {
    idx1: usize = 0,
    item: u8 = 0,
    idx2: usize = 0,
    victim: []u8,
    buckets: []usize,
    hex: []u8 = &[0]u8{},
};

const Counter = struct {
    pub fn unwrap(comptime arg: *Arg) u8 {
        arg.buckets[arg.victim[arg.idx1]] += 1;
        arg.idx1 += 1;
        return 0;
    }
};

const Writer = struct {
    pub fn unwrap(comptime arg: *Arg) u8 {
        arg.victim[arg.idx2] = arg.item;
        arg.idx2 += 1;
        return 0;
    }
};

const Sorter = struct {
    pub fn unwrap(comptime arg: *Arg) u8 {
        arg.item = arg.idx1;
        _ = Loop(arg, Writer.unwrap, arg.buckets[arg.idx1]);
        arg.idx1 += 1;
        return 0;
    }
};

const Hex = struct {
    pub fn unwrap(comptime arg: *Arg) u8 {
        const table = "0123456789abcdef";
        arg.hex[arg.idx1 * 2 + 0] = table[arg.victim[arg.idx1] >> 4];
        arg.hex[arg.idx1 * 2 + 1] = table[arg.victim[arg.idx1] & 0x0F];
        arg.idx1 += 1;
        return 0;
    }
};

pub fn main() !void {
    comptime {
        var input = [0]u8{};
        var scratch = [_]usize{0} ** (1 << @bitSizeOf(u8));
        var hex = [_]u8{0} ** (input.len * 2);
        var argument = Arg{
            .victim = &input,
            .buckets = &scratch,
            .hex = &hex,
        };
        _ = Loop(&argument, Counter.unwrap, input.len);
        argument.idx1 = 0;
        _ = Loop(&argument, Sorter.unwrap, scratch.len);
        argument.idx1 = 0;
        _ = Loop(&argument, Hex.unwrap, input.len);

        @compileError(&hex);
    }
}
