#include <arpa/inet.h>
#include <netinet/in.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

#include "common.h"

#define EOS     -1


int main(void) {
    struct sockaddr_in address = {0};
    socklen_t size = sizeof(struct sockaddr_in);


    int fdsocket = socket(AF_INET, SOCK_DGRAM, 0);
#ifdef DEBUG
    debug_check_error("socket", __FILE__, __LINE__);
#else
    check_error("socket");
#endif


    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(HOST_PORT);
    bind(fdsocket, (void*) &address, size);
#ifdef DEBUG
    debug_check_error("bind", __FILE__, __LINE__);
#else
    check_error("bind");
#endif


    while(1) {
        char buffer[PACSIZ] = {0};
        struct sockaddr sender = {0};


        recvfrom(fdsocket, buffer, PACSIZ, 0, &sender, &size);
#ifdef DEBUG
        debug_check_error("recvfrom", __FILE__, __LINE__);
#else
        check_error("recvfrom");
#endif


        if (!strncmp(buffer, "disconnect", 10)) {
            close(fdsocket);
#ifdef DEBUG
            debug_check_error("close", __FILE__, __LINE__);
#else
            check_error("close");
#endif
            return EXIT_SUCCESS;
        }
        else if (strlen(buffer) > 0) {
            printf("= %s\n", buffer);
        }
    }

    return EXIT_SUCCESS;
}
