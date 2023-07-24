# zipper

## Author: flocto

**Solves:** 101

**Points:** 431

---

Stare into the zip and the zip stares back.

---

**Provided Files:**

- [flag.zip](./flag.zip)

## Solution

Check [main.py](main.py) for more details. 

There are four main parts to this one.

### Part 1
Stored as a comment in the zip file. General zip file comments are stored at the very end.
```
Part 1: amateursCTF{z1PP3d_
```

### Part 3
Stored as a comment of a specific file in the zip. These comments are placed in the middle, but a simple plaintext search works fine (`strings`)
```
Part 3: laY3r_0f
```

The PK is ignored since it marks the start of the file data. Also note that this file should seemingly be named `flag/Part 3: laY3r_0f`, but no such file exists in the zip. We'll get to that later.

### Part 4
Out of the 1035 files inside `flag/`, 10 are red herrings named `flag/../flag` that do nothing. 

The remaining 1025 are all numbers from 0 to 1023. Only one of these is a duplicate, and since zips treat duplicates as overwriting, the Part 4 data is overwritten when it is extracted.
```
Part 4: _Zips}
```

### Part 2
Back to the weird file that Part 3 is on. This is actually a text file NAMED `flag/`, but since the `flag/` directory exists BEFORE this file is referenced in the zip file, it is ignored and does not overwrite the directory, unlike how files overwrite files. Additionally, it isn't recognized by many zip GUI programs, so it won't show up there either.

The only way to get this part is to again extract manually. See solve script.
```
Part 2: in5id3_4_
```

Full flag:
```
amateursCTF{z1PP3d_in5id3_4_laY3r_0f_Zips}
```