#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#ifdef DEBUG
void debug_check_error(char *str, char *file, int line) {
    if (errno) {
        fprintf(stderr, "[%s:%d] %s: %s\n", file, line, str, strerror(errno));
        exit(EXIT_FAILURE);
    }
}


void debug_check_error2(char *str, char *extra, char *file, int line) {
    if (errno) {
        fprintf(stderr, "[%s:%d] %s: %s (%s)\n", file, line, str, strerror(errno), extra);
        exit(EXIT_FAILURE);
    }
}
#endif


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
