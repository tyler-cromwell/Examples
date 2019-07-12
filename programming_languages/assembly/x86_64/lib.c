#include <stdio.h>

extern void asm_hello(void);


int c_hello(void) {
    asm_hello();
    return printf("Hello from C!\n");
}
