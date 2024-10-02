#include <stdio.h>
#include <windows.h>
#include <msdelta.h>
#pragma comment(lib, "msdelta.lib")

static char patch[93] = "\x50\x41\x33\x30\xc0\x08\x97\xfc\xfd\x3c\xda\x01\x18\x23\x68\x83\x04\x80\x52\x00larry-killed-this!!!\x01\xca\x00\xb7\x03\x88\x69\xb3\xfa\xf4\x89\x36\xa5\xdd\x8c\x01\xd1\xda\x4d\x88\x11\x69\x4c\xbb\x71\x7d\xda\x75\x6a\x37\x2a\xd2\x88\x11\x91\x22\x4e\x66\xde\xa0\x31\x3d\x22\xcc\x9b\xd6\xae\x47\xb4\x39\xb1\x56\x01";
// first byte of hash 2d -> 2c

int main() {
    char* input = (char*)malloc(100);
    printf("What is the flag?\n> ");
    
    fgets(input, 100, stdin);

    size_t len = strcspn(input, "\n");
    if (len != 54) {
        puts("Wrong!");
        return 1;
    }

    if (strncmp(input, "amateursCTF{", 12) != 0 || input[53] != '}') {
        puts("Wrong!");
        return 1;
    }

    DELTA_INPUT input_struct;
    input_struct.Editable = TRUE;
    input_struct.lpcStart = input;
    input_struct.uSize = len;

    DELTA_INPUT delta_patch;
    delta_patch.Editable = TRUE;
    delta_patch.lpStart = patch;
    delta_patch.uSize = sizeof(patch);

    DELTA_OUTPUT output;

    BOOL res = ApplyDeltaB(0, input_struct, delta_patch, &output);
    if (res){
        puts("Correct, here's your flag: ");
        printf("%s\n", (char *) output.lpStart);
        DeltaFree(output.lpStart);
    }
    else {
        puts("Wrong!");
        DeltaFree(output.lpStart);
    }

    return 0;
}