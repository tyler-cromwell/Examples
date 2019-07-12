BITS 64

extern  printf
extern  c_hello

global  main
global asm_hello


        section .data
fmtd:   db  "%d", 0x0a, 0x00
hello:  db  "Hello from ASM", 0x21, 0x0a, 0x00


        section .text
main:
        ; Allocate new stack frame
        push rbp
        mov rbp, rsp

        ; Call function
        call c_hello
        push rax            ; Save result

        ; Print the return value from say_hello()
        mov rax, 0
        mov rdi, fmtd
        mov rsi, [rsp]
        call printf

        ; Deallocate stack frame
        mov rsp, rbp    ;
        pop rbp
        ret

asm_hello:
        ; Allocate new stack frame
        push rbp
        mov rbp, rsp

        ; Print string
        mov rax, 0
        mov rdi, hello
        call printf  

        ; Deallocate stack frame
        mov rsp, rbp    ;
        pop rbp
        ret
