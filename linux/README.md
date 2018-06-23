# Linux
Example of a basic [Linux][linux] [kernel module][module].

To build and install, execute `[make]` and insert the module object file (`.ko`):
```
$ make
$ sudo insmod linuxmod.ko
```

Remove module using just the name:

`$ sudo rmmod linuxmod`


[linux]: https://en.wikipedia.org/wiki/Linux
[make]: https://www.gnu.org/software/make/
[module]: https://en.wikipedia.org/wiki/Loadable_kernel_module#Linux
