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
    struct sockaddr_in address = {0};


    // Create socket (IPv4, TCP)
    int fdsocket = socket(AF_INET, SOCK_STREAM, 0);
#ifdef DEBUG
    debug_check_error("socket", __FILE__, __LINE__);
#else
    check_error("socket");
#endif


    // Specify server address
    address.sin_family = AF_INET;           // IPv4
    address.sin_port = htons(HOST_PORT);
    inet_pton(AF_INET, HOST_IP, &address.sin_addr);
#ifdef DEBUG
    debug_check_error("inet_pton", __FILE__, __LINE__);
#else
    check_error("inet_pton");
#endif


    // Open a connection to the server
    connect(fdsocket, (void*) &address, sizeof(struct sockaddr_in));
#ifdef DEBUG
    debug_check_error2("connect", "Server is down", __FILE__, __LINE__);
#else
    check_error2("connect", "Server is down");
#endif


    // Send a message
    send(fdsocket, "Hello, world!", 14, 0);
#ifdef DEBUG
    debug_check_error("send", __FILE__, __LINE__);
#else
    check_error("send");
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
                send(fdsocket, buffer, PACSIZ, 0);
#ifdef DEBUG
                debug_check_error("send", __FILE__, __LINE__);
#else
                check_error("send");
#endif
                break;
            }
        }
    }


    // Terminate connection
    close(fdsocket);
#ifdef DEBUG
    debug_check_error("close", __FILE__, __LINE__);
#else
    check_error("close");
#endif
    return EXIT_SUCCESS;
}
