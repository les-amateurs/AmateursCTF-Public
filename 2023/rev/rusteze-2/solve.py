item = b'\xc0\xa7\xe5\xb7\x03\x46\x35\x26\xae\x1a\x37\xd4\x98\xda\x39\x17\x88\xe3\x7d\x8f\xf2\xae\x19\x49\x0e\xdc\xe9\x36\x82\x5f'
stuff = [
   0xd2, 0xa5, 0xf6, 0xb1, 0x1f, 0x6c, 0x33, 0x3d, 0x84, 0x3d, 0x2e, 0xc6, 0x8f, 0x84, 0x23, 0x7b, 0xa3, 0xbf, 0x76, 0xb4, 0xcb, 0xa6, 0x1d, 0x7c, 0x24, 0xdb, 0xf5, 0x6c, 0x95, 0x7d, 0x56, 0x61, 0x85, 0x4d, 0x2f
]

fill = b'sorry_this_isnt_the_flag_this_time.'

flag = bytes([fill[i] ^ stuff[i] ^ item[i] for i in range(len(item))])
print(flag)

# theres weird xor in enc logic, investigate
'''
    local_39 = *(byte *)(param_2 + uVar3) ^ local_93[uVar3];
    if (uVar3 < 0x1e) {
      if (0x1d < uVar3) {
        FUN_140023bf0(uVar3,0x1e,&PTR_s_src\main.rs_140025678);
        goto LAB_140002b5d;
      }
      bVar1 = (&DAT_140030000)[uVar3];
      (&DAT_140030000)[uVar3] = local_39 ^ bVar1;
      uVar3 = CONCAT71((int7)(uVar3 >> 8),local_39 ^ bVar1);
    }
'''