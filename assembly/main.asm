BITS 64

extern  printf
extern  say_hello


        section .text
fmtd:   db  "%d", 0xa, 0x0


        section .text
        global  main
main:
        push rbp
        mov rbp, rsp
        call say_hello      ; result in rax

        ; Print the result "say_hello"
        push rax        ; Save integer
        mov rax, 0
        mov rdi, fmtd   ; Format (integer)
        mov rsi, [rsp]  ; Integer
        call printf

        mov rsp, rbp
        pop rbp

        mov rax, 60     ; Exit
        mov rdi, 0
        syscall
