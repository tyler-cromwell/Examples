#include <unistd.h>
#include <sys/syscall.h>


void _start() {
    static const char message[] = "Hello world!\n";
    size_t length = sizeof(message)-1;
    syscall(SYS_write, 1, message, length);
    syscall(SYS_exit, 0);
}
