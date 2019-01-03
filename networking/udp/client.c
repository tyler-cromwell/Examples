#define _GNU_SOURCE

#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

#include "common.h"


int main(void) {
    char buffer[PACSIZ] = {0};
    struct sockaddr_in remote;
    socklen_t size = sizeof(struct sockaddr_in);


    // Create socket (IPv4, UDP)
    int fdsocket = socket(AF_INET, SOCK_DGRAM, 0);
#ifdef DEBUG
    debug_check_error("socket", __FILE__, __LINE__);
#else
    check_error("socket");
#endif


    // Bind
    remote.sin_family = AF_INET;            // IPv4
    remote.sin_port = htons(HOST_PORT);
    remote.sin_addr.s_addr = INADDR_ANY;    // Accept from any interface on the machine
    inet_pton(AF_INET, HOST_IP, &remote.sin_addr);
#ifdef DEBUG
    debug_check_error("inet_pton", __FILE__, __LINE__);
#else
    check_error("inet_pton");
#endif


    // Send a message
    sendto(fdsocket, "Hello, world!", 14, 0, &remote, size);
#ifdef DEBUG
    debug_check_error("sendto", __FILE__, __LINE__);
#else
    check_error("sendto");
#endif


    // Wait for and send user input
    while ((strncmp(buffer, "disconnect", 10) || strlen(buffer) != 10) &&
           (strncmp(buffer, "shutdown", 8) || strlen(buffer) != 8)) {
        memset(buffer, '\0', PACSIZ);
        char *result = fgets(buffer, PACSIZ-1, stdin);
#ifdef DEBUG
        debug_check_error("fgets", __FILE__, __LINE__);
#else
        check_error("fgets");
#endif


        if (result == NULL) {
            break;
        }

        for (size_t i = 0; i < PACSIZ; i++) {
            if (buffer[i] == '\n') {
                buffer[i] = '\0';
                sendto(fdsocket, buffer, PACSIZ, 0, &remote, size);
#ifdef DEBUG
                debug_check_error("sendto", __FILE__, __LINE__);
#else
                check_error("sendto");
#endif
                break;
            }
        }
    }


    // Terminate
    close(fdsocket);
#ifdef DEBUG
    debug_check_error("close", __FILE__, __LINE__);
#else
    check_error("close");
#endif
    return EXIT_SUCCESS;
}
