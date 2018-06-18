#include <arpa/inet.h>
#include <errno.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

#include "common.h"


int main(void) {
    errno = 0;
    char buffer[PACSIZ] = {0};
    struct sockaddr_in address;
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    check_error("socket");

    address.sin_family = AF_INET;
    address.sin_port = htons(HOST_PORT);
    check_error("htons");

    inet_pton(AF_INET, HOST_IP, &address.sin_addr);
    check_error("inet_pton");

    connect(sock, (void*) &address, sizeof(struct sockaddr_in));
    check_error2("connect", "Server is down");

    send(sock, "Hello, world!", 14, 0);
    check_error("send");

    while ((strncmp(buffer, "disconnect", 10) || strlen(buffer) != 10) &&
           (strncmp(buffer, "shutdown", 8) || strlen(buffer) != 8)) {
        memset(buffer, '\0', PACSIZ);
        check_error("memset");

        if (fgets(buffer, PACSIZ-1, stdin) == NULL) {
            break;
        }

        for (size_t i = 0; i < PACSIZ; i++) {
            if (buffer[i] == '\n') {
                buffer[i] = '\0';
                send(sock, buffer, PACSIZ, 0);
                check_error("send");
                break;
            }
        }
    }

    close(sock);
    check_error("close");
    return EXIT_SUCCESS;
}
