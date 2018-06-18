#ifndef COMMON_H
#define COMMON_H

#include <errno.h>
#include <stdio.h>
#include <string.h>

#define HOST_IP     "127.0.0.1"
#define HOST_PORT   8080
#define PACSIZ      1024


void check_error(char *str) {
    if (errno) {
        fprintf(stderr, "%s: %s\n", str, strerror(errno));
        exit(EXIT_FAILURE);
    }
}


void check_error2(char *str, char *extra) {
    if (errno) {
        fprintf(stderr, "%s: %s (%s)\n", str, strerror(errno), extra);
        exit(EXIT_FAILURE);
    }
}

#endif
