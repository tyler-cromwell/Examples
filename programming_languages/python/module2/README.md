# Python C/C++ extension module
This is an example of how to build, debug, and use a C/C++ extension module for Python 2.

## Build and Installation
| Command                        | Purpose                                                                                       |
|:------------------------------:|:---------------------------------------------------------------------------------------------:|
| `python setup.py build`        | Compiles the module.                                                                          |
| `sudo python setup.py install` | Installs the module (append `--record files.txt` to record the paths of the installed files). |

## Debugging
The Debugging process is as follows:
1. Build a debug version of Python.
    1. `./configure --without-pymalloc --with-valgrind --with-pydebug --prefix=\``pwd``/build`
2. Install module with/to the debug interpreter.
    1. `sudo ~/Sources/cpython/python setup.py install --record files.txt`
3. Run valgrind on the debug interpreter.
    1. **BE SURE TO RECORD THE BASE LEAK VALUES BEFORE RUNNING YOUR MODULE**
    2. Run module and observe any changes in leak values.
4. (Optional) Uninstall module.
    1. `cat files.txt | xargs sudo rm -rf`

## Usage
```
>>> import c
>>> c.add(4, 5, 2.71, 3.14)
14.850000000000001
>>> c.printf('%s\n%d\n', 'Hello, world!', 42)
Hello, world!
42
>>>
```

## Requirments
- Python 2.7
- Distutils
- C compiler

## Short notes
- The module initialization function **must** be named `init` followed by the name for the `import` statement.
- Object allocation/deallocation works using [reference counting][refcnt]. Objects with a reference count of `0` will be deallocated.
- "New" references that are returned to the interpreter will later be cleaned up by it.
- "Borrowed" references should be accompanied by calls to `Py_INCREF` and `Py_DECREF`.


[refcnt]: https://docs.python.org/2/c-api/intro.html#objects-types-and-reference-counts
