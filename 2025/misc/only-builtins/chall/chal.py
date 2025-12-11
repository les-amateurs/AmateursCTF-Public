#!/usr/bin/env python3

import tempfile
import subprocess
import re

src = input("> ")
if not re.match(r"^(?:__auto_type v\d+=__builtin_[a-z_]+\((?:v\d+(?:,v\d+)*)?\);)+$", src):
    print("only builtins")
    exit(1)

with tempfile.TemporaryDirectory(dir="/tmp/work") as tmpdirname:
    with open(f"{tmpdirname}/main.c", "w") as f:
        f.write(f"#include<stdio.h>\nint main(){{setvbuf(stdout,NULL,_IONBF,0);setvbuf(stdin,NULL,_IONBF,0);{src}}}")

    ret = subprocess.run(
        ["gcc", f"{tmpdirname}/main.c", "-o", f"{tmpdirname}/main"],
        capture_output=True,
    )
    if ret.returncode != 0:
        print("compilation error")
        exit(1)

    ret = subprocess.run(
        [f"{tmpdirname}/main"],
        stderr=subprocess.DEVNULL,
    )
    if ret.returncode != 0:
        print("runtime error")
        exit(1)
