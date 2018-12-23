#include <stdio.h>


int main(void) {
    puts("Hello world!");
#if DEBUG
    puts("This is the DEBUG executable.");
#else
    puts("This is the RELEASE executable.");
#endif
    return 0;
}
