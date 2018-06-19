#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#include "common.h"


int main(int argc, char *argv[]) {
    // Construct pipe for Inter-Process Communication
    int pfds[2];
    pipe(pfds);

    // Clone process
    pid_t cpid = fork();

    switch (cpid) {
        // Child process
        case 0: {
            // Close read end of the pipe
            close(pfds[0]);

            // Direct STDOUT to the write end of the pipe
            close(STDOUT_FILENO);
            dup2(pfds[1], STDOUT_FILENO);
            close(pfds[1]);

            // Prepare arguments for the child
            char *cargv[] = {
                "./arithmetic",
                argv[1],
                argv[2],
                argv[3],
                NULL
            };

            // Load and execute child program
            execvp(cargv[0], cargv);
            break;
        }
        // Parent process
        default: {
            // Close write end of the pipe
            close(pfds[1]);

            // Wait for child to complete
            waitpid(cpid, NULL, 0);
        }
    }

    // Read output of the child process from the pipe
    char buffer[1024] = {0};
    read(pfds[0], buffer, 1024);
    printf("%d\n", atoi(buffer));
    close(pfds[0]);
    return EXIT_SUCCESS;
}
