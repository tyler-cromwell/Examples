#include <stdio.h>
#include <stdlib.h>

#include "common.h"


int main(int argc, char *argv[]) {
    if (argc != 4) {
        fprintf(stdout, "none");
        return EXIT_FAILURE;
    }

    int m = atoi(argv[1]);
    int n = atoi(argv[2]);
    op_t op = atoi(argv[3]);

    switch (op) {
        case ADD:
            fprintf(stdout, "%d", m + n);
            break;
        case SUB:
            fprintf(stdout, "%d", m - n);
            break;
        case MUL:
            fprintf(stdout, "%d", m * n);
            break;
        case DIV:
            if (n == 0) {
                fprintf(stdout, "infinity");
            } else {
                fprintf(stdout, "%d", m / n);
            }
            break;
    }

    return EXIT_SUCCESS;
}
