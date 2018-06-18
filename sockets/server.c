#include <assert.h>
#include <errno.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

#include "common.h"

#define BACKLOG 0
#define EOS     -1


int main(void) {
    int enable = 1;
    struct sockaddr_in address;
    socklen_t size = sizeof(struct sockaddr_in);
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    check_error("socket");

    setsockopt(sock, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &enable, sizeof(enable));
    check_error("setsockopt");

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(HOST_PORT);
    check_error("htons");

    bind(sock, (void*) &address, size);
    check_error("bind");

    listen(sock, BACKLOG);
    check_error("listen");

    while (1) {
        int connection = accept(sock, (void*) &address, (socklen_t*) &size);
        check_error("accept");
        printf("# Accepted connection %d\n", connection);

        while (1) {
            char buffer[PACSIZ] = {0};

            for (size_t i = 0; i < PACSIZ; i++) {
                char c = EOS;
                recv(connection, &c, sizeof(char), 0);
                check_error("recv");
                if (c == '\0') {break;}
                buffer[i] = c;
            }

            if (!strncmp(buffer, "disconnect", 10) || buffer[0] == EOS) {
                break;
            } else if (!strncmp(buffer, "shutdown", 8) || buffer[0] == EOS) {
                close(sock);
                check_error("close");
                printf("# Connections terminated, goodbye\n");
                return EXIT_SUCCESS;
            } else if (strlen(buffer) > 0 && buffer[0] != EOS) {
                printf("= %s\n", buffer);
            }
        }

        close(connection);
        check_error("close");
        printf("# Terminated connection %d\n", connection);
    }

    return EXIT_FAILURE;
}
