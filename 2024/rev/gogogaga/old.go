package main

import (
	"encoding/base64"
	"encoding/hex"
	"fmt"
)

// amateursCTF{c4nt_b3liev3_g0_ogl3_clos3d_CTF_sp0n50rs}

//go:noinline
func Monday(flag string) bool {
	return len(flag) == 53
}

//go:noinline
func Tuesday(flag string) bool {
	return flag[0:12] == "amateursCTF{" && flag[52:53] == "}"
}

//go:noinline
func Wednesday(flag string) bool {
	return base64.StdEncoding.EncodeToString([]byte(flag[12:25])) == "YzRudF9iM2xpZXYzXw=="
}

//go:noinline
func Thursday(flag string) bool {
	return hex.EncodeToString([]byte(flag[25:40])) == "67305f6f676c335f636c6f7333645f"
}

//go:noinline
func Friday(flag string) bool {
	var buf []byte = []byte(flag[40:52])
	for i := 0; i < len(buf); i++ {
		buf[i] = buf[i] ^ 0xa2
	}
	return string(buf) == "\xe1\xf6\xe4\xfd\xd1\xd2\x92\xcc\x97\x92\xd0\xd1"
}

//go:noinline
func checkFlag(flag string) bool {
	if Monday(flag) {
		if Tuesday(flag) {
			if Wednesday(flag) {
				if Thursday(flag) {
					if Friday(flag) {
						return true
					}
				}
			}
		}
	}
	return false
}

func main() {
	fmt.Println("What's the flag?")
	fmt.Print("> ")
	var input string
	fmt.Scanln(&input)

	if checkFlag(input) {
		fmt.Println("Looks good to me!")
	} else {
		fmt.Println("Try again!")
	}
}
