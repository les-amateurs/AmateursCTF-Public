package main

import (
	"encoding/base64"
	"fmt"
	"os"
	"strings"
)

// amateursCTF{c4nt_b3liev3_g0_ogl3_clos3d_CTF_sp0n50rs}

//go:noinline
func Monday(key string, check chan bool) {
	check <- base64.StdEncoding.EncodeToString([]byte(key)) == "TEFSUlk="
}

//go:noinline
func Tuesday(key string, check chan bool) {
	s := 0
	for i := 0; i < 5; i++ {
		if key[i] < '0' || key[i] > '9' {
			check <- false
			return
		}
		s += int(key[i] - '0')
	}
	check <- s == 35
}

//go:noinline
func Wednesday(key string, check chan bool) {
	seen := make(map[byte]bool)
	for i := 0; i < 5; i++ {
		if key[i] < 'A' || key[i] > 'Z' {
			check <- false
			return
		}
		if seen[key[i]] {
			check <- false
			return
		}
		seen[key[i]] = true
	}

	key_xor := []byte(key)
	for i := 0; i < 5; i++ {
		key_xor[i] = key_xor[i] ^ 0x60
	}
	Tuesday(string(key_xor), check)
}

//go:noinline
func Thursday(key string, check chan bool) {
	key_enc := []byte(key)
	x, y := 0, 0
	for i := 0; i < 5; i++ {
		k := key_enc[i]
		for k != 0 {
			if k&1 == 1 {
				x++
			} else {
				x--
			}
			if k&2 == 2 {
				y++
			} else {
				y--
			}
			k >>= 2
		}
	}
	check <- x == 5 && y == 3
}

//go:noinline
func Friday(key string, check chan bool) {
	unlock := []byte("UNL0CK")
	dp := make([][]uint, 6)
	for i := 0; i < 6; i++ {
		dp[i] = make([]uint, 7)
	}
	for i := 0; i < 6; i++ {
		dp[i][0] = uint(i)
	}
	for j := 0; j < 7; j++ {
		dp[0][j] = uint(j)
	}

	// levenshtein distance
	for i := 1; i < 6; i++ {
		for j := 1; j < 7; j++ {
			if key[i-1] == unlock[j-1] {
				dp[i][j] = dp[i-1][j-1]
			} else {
				dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
			}
		}
	}
	check <- dp[5][6] == 3
}

//go:noinline
func checkKey(key string) bool {
	var key_parts []string = strings.Split(key, "-")
	if len(key_parts) != 5 {
		return false
	}
	for i := 0; i < 5; i++ {
		if len(key_parts[i]) != 5 {
			return false
		}
		for j := 0; j < 5; j++ {
			// A-Z0-9
			if key_parts[i][j] < 'A' || key_parts[i][j] > 'Z' {
				if key_parts[i][j] < '0' || key_parts[i][j] > '9' {
					return false
				}
			}
		}
	}

	check := make(chan bool, 5)
	go Monday(key_parts[0], check)
	go Tuesday(key_parts[1], check)
	go Wednesday(key_parts[2], check)
	go Thursday(key_parts[3], check)
	go Friday(key_parts[4], check)

	for i := 0; i < 5; i++ {
		if !<-check {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println("Gimme a key.")
	fmt.Print("> ")
	var input string
	fmt.Scanln(&input)

	if checkKey(input) {
		fmt.Println("Looks good to me!")
		fmt.Print("Here's your flag: ")
		flag, err := os.ReadFile("flag.txt")
		if err != nil {
			fmt.Println("Error reading flag.txt. Contact an admin if you are on the server.")
			return
		}
		os.Stdout.Write(flag)
		fmt.Println()
	} else {
		fmt.Println("Try again!")
	}
}
