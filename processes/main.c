#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#include "common.h"


int main(int argc, char *argv[]) {
    int pfds[2];
    pipe(pfds);

    pid_t cpid = fork();

    switch (cpid) {
        case 0: {
            close(pfds[0]);

            close(STDOUT_FILENO);
            dup2(pfds[1], STDOUT_FILENO);
            close(pfds[1]);

            char *cargv[] = {
                "./arithmetic",
                argv[1],
                argv[2],
                argv[3],
                NULL
            };

            execvp(cargv[0], cargv);
            break;
        }
        default: {
            close(pfds[1]);
            waitpid(cpid, NULL, 0);
        }
    }

    char buffer[1024] = {0};
    read(pfds[0], buffer, 1024);
    printf("%d\n", atoi(buffer));
    close(pfds[0]);
    return EXIT_SUCCESS;
}
