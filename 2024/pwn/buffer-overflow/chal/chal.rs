use std::mem::ManuallyDrop;
use std::ptr;
use std::slice;
use std::str;

#[inline(never)]
#[no_mangle]
pub extern "C" fn uppercase(src: *const u8, srclen: usize, dst: *mut u8) {
    unsafe {
        let upper = ManuallyDrop::new(
            str::from_utf8(slice::from_raw_parts(src, srclen))
                .unwrap()
                .to_uppercase(),
        );
        let bytes = upper.as_bytes();

        let bytes_ptr = bytes.as_ptr();

        ptr::copy_nonoverlapping(bytes_ptr, dst, bytes.len());
    }
}
