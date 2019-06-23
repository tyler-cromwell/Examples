# Hello World (no libc)
This is an example of how to write a [C][c] program without the use of the C [Standard Libary][stdlib].
This is also the C analogue of the [assembly][asm] code in [`Examples/assembly/x86_64/main.asm`][asmcode].

## Compilation
Execute: `$ gcc -static -nostartfiles hello.c -o hello`.


[asm]: https://en.wikipedia.org/wiki/Assembly_language
[asmcode]: https://github.com/tyler-cromwell/Examples/blob/master/assembly/x86_64/main.asm
[c]: https://en.wikipedia.org/wiki/C_(programming_language)
[stdlib]: https://en.wikipedia.org/wiki/Standard_library
