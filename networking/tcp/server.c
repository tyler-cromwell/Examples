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


    // Create socket (IPv4, TCP)
    int fdsocket = socket(AF_INET, SOCK_STREAM, 0);
#ifdef DEBUG
    debug_check_error("socket", __FILE__, __LINE__);
#else
    check_error("socket");
#endif


    // Force (re)use of the IP address and port number.
    setsockopt(fdsocket, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &enable, sizeof(enable));
#ifdef DEBUG
    debug_check_error("setsockopt", __FILE__, __LINE__);
#else
    check_error("setsockopt");
#endif


    // Bind
    address.sin_family = AF_INET;           // IPv4
    address.sin_addr.s_addr = INADDR_ANY;   // Accept connections from any interface on the machine
    address.sin_port = htons(HOST_PORT);
    bind(fdsocket, (void*) &address, size);
#ifdef DEBUG
    debug_check_error("bind", __FILE__, __LINE__);
#else
    check_error("bind");
#endif


    // Listen for connections
    listen(fdsocket, BACKLOG);
#ifdef DEBUG
    debug_check_error("listen", __FILE__, __LINE__);
#else
    check_error("listen");
#endif


    while (1) {
        // Wait for a request from a client
        int fdconnection = accept(fdsocket, (void*) &address, (socklen_t*) &size);
#ifdef DEBUG
        debug_check_error("accept", __FILE__, __LINE__);
#else
        check_error("accept");
#endif
        printf("# Accepted connection %d\n", fdconnection);


        // Handle connection
        while (1) {
            char buffer[PACSIZ] = {0};

            for (size_t i = 0; i < PACSIZ; i++) {
                char c = EOS;
                recv(fdconnection, &c, sizeof(char), 0);
#ifdef DEBUG
                debug_check_error("recv", __FILE__, __LINE__);
#else
                check_error("recv");
#endif
                if (c == '\0') {break;}
                buffer[i] = c;
            }

            if (!strncmp(buffer, "disconnect", 10) || buffer[0] == EOS) {
                break;
            } else if (!strncmp(buffer, "shutdown", 8) || buffer[0] == EOS) {
                close(fdsocket);
#ifdef DEBUG
                debug_check_error("close", __FILE__, __LINE__);
#else
                check_error("close");
#endif
                printf("# Connections terminated, goodbye\n");
                return EXIT_SUCCESS;
            } else if (strlen(buffer) > 0 && buffer[0] != EOS) {
                printf("= %s\n", buffer);
            }
        }


        // Terminate connection
        close(fdconnection);
#ifdef DEBUG
        debug_check_error("close", __FILE__, __LINE__);
#else
        check_error("close");
#endif
        printf("# Terminated connection %d\n", fdconnection);
    }

    return EXIT_FAILURE;
}
