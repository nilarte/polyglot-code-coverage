#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("Number of arguments: %d\n", argc);

    if (argc > 1) {
        printf("First argument: %s\n", argv[1]);
    } else {
        printf("No arguments provided.\n");
    }

    return 0;
}