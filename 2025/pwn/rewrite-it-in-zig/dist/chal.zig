const std = @import("std");
const print = std.debug.print;

pub fn main() void {
    print("you can never have too much zig pwn.\n", .{});

    var backing: [0x100]u8 = undefined;
    var buf: []u8 = &backing;
    buf.len = 0x1000;
    _ = std.io.getStdIn().read(buf) catch {};
}
