#include <stdio.h>


void say_hello(void) {
    puts("Hello world!");
#if DEBUG
    puts("This is the DEBUG library.");
#else
    puts("This is the RELEASE library.");
#endif
}
