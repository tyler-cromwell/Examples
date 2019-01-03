#ifndef COMMON_H
#define COMMON_H

#include <stdio.h>

#define HOST_IP     "127.0.0.1"
#define HOST_PORT   8080
#define PACSIZ      1024

#ifdef DEBUG
extern void debug_check_error(char *str, char *file, int line);
extern void debug_check_error2(char *str, char *extra, char *file, int line);
#endif
extern void check_error(char *str);
extern void check_error2(char *str, char *extra);

#endif
