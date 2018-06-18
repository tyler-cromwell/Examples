#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#include "common.h"


pid_t execute(char *args[], int fdin, int fdout) {
    pid_t prog = fork();

    switch (prog) {
        case 0:
            if (fdin != -1) {
                close(STDIN_FILENO);
                dup2(fdin, STDIN_FILENO);
                close(fdin);
            }

            if (fdout != STDOUT_FILENO) {
                close(STDOUT_FILENO);
                dup2(fdout, STDOUT_FILENO);
                close(fdout);
            }

            execvp(args[0], args);
            return -1;
        default:
            close(fdout);
            return prog;
    }
}


int main(int argc, char *argv[]) {
//    cat /dev/urandom| tr -dc '0-9a-zA-Z!@#$%^&*_+-'|head -c 8
    //char *args1[] = {"dd", "bs=1K", "count=1", "if=/dev/urandom", NULL};
    char *args1[] = {"cat", "string.txt", NULL};
    char *args2[] = {"sed", "s/e/z/g", NULL};
    char *args3[] = {"sed", "s/o/z/g", NULL};
    char *args4[] = {"sed", "s/a/z/g", NULL};

    // Create pipes
    int p1[2];  pipe(p1);
    int p2[2];  pipe(p2);
    int p3[2];  pipe(p3);
    int p4[2];  pipe(p4);

    // Start programs

    pid_t prog1 = execute(args1, -1, p1[1]);
    pid_t prog2 = execute(args2, p1[0], p2[1]);
    pid_t prog3 = execute(args3, p2[0], p3[1]);
    pid_t prog4 = execute(args4, p3[0], STDOUT_FILENO);

    waitpid(prog1, NULL, 0);
    waitpid(prog2, NULL, 0);
    waitpid(prog3, NULL, 0);
    waitpid(prog4, NULL, 0);

    return EXIT_SUCCESS;
}
