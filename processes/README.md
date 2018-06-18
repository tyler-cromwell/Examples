# Processes
Examples of process forking, piping, program execution, and stream redirection.

## Main
Pipes arguments to the child process `arithmetic`. Four operations (third integer):

Addition:
```
$ ./main 7 5 0
12
```

Subtraction:
```
$ ./main 7 5 1
2
```

Multiplication:
```
$ ./main 2 4 2
8
```

Division:
```
$ ./main 8 2 3
4
```

# Pipeline
Constructs a pipeline through which the contents of `string.txt` flow and are altered three 3 times by `sed`. The result is printed to a `stdout`.
