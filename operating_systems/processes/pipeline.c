#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#include "common.h"


pid_t execute(char *args[], int fdin, int fdout) {
    // Clone process
    pid_t prog = fork();

    switch (prog) {
        // Child process
        case 0:
            if (fdin != -1) {
                // Redirect STDIN to the given file
                close(STDIN_FILENO);
                dup2(fdin, STDIN_FILENO);
                close(fdin);
            }

            if (fdout != STDOUT_FILENO) {
                // Redirect STDOUT to the given file
                close(STDOUT_FILENO);
                dup2(fdout, STDOUT_FILENO);
                close(fdout);
            }

            // Load and execute child program
            execvp(args[0], args);
            return -1;
        // Parent process
        default:
            close(fdout);
            return prog;
    }
}


int main(int argc, char *argv[]) {
    // Prepare arguments for each child
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

    // Wait for each stage of the pipeline (i.e. wait for each child)
    waitpid(prog1, NULL, 0);
    waitpid(prog2, NULL, 0);
    waitpid(prog3, NULL, 0);
    waitpid(prog4, NULL, 0);
    return EXIT_SUCCESS;
}
