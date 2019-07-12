// Python 2.7
#include <stdio.h>

#include <Python.h>


static PyObject * c_add(PyObject *self, PyObject *args) {
    Py_ssize_t argc = PyTuple_Size(args);
    PyObject *sum = PyFloat_FromDouble(0); // Initialize to zero

    // Sum all given operands
    for (Py_ssize_t i = 0; i < argc; i++) {
        PyObject *number = PyTuple_GetItem(args, i);
        PyObject *temp = PyNumber_Add(sum, number);

        if (temp == NULL) {
            PyErr_SetString(PyExc_ArithmeticError, "failed to add");
            return NULL;
        } else {
            // Dealloc old sum and save new
            Py_DECREF(sum);
            sum = temp;
        }
    }

    return sum;
}


static PyObject * c_printf(PyObject *self, PyObject *args) {
    Py_ssize_t argc = PyTuple_Size(args);

    // Check argument count
    if (argc < 1) {
        PyErr_Format(PyExc_TypeError, "c_printf() takes at least two arguments (%lu given)", argc);
        return NULL;
    }

    // Perform C-style printf
    PyObject *format = PyTuple_GetItem(args, 0);
    PyObject *values = PyTuple_GetSlice(args, 1, argc);
    PyObject *string = PyString_Format(format, values);
    PyObject_Print(string, stdout, Py_PRINT_RAW);

    // Clean up
    Py_DECREF(values);
    Py_DECREF(string);
    Py_RETURN_NONE;
}


static PyObject * c_version(PyObject *self, PyObject *args) {
    return Py_BuildValue("s", FULL_VERSION);
}


static PyMethodDef CMethods[] = {
    {"add", c_add, METH_VARARGS, "Returns the sum of given oprands."},
    {"printf", c_printf, METH_VARARGS, "Formatted print."},
    {"version", c_version, METH_NOARGS, "Returns module version."},
    {NULL, NULL, 0, NULL}
};


PyMODINIT_FUNC initc(void)  {
    PyObject *module = Py_InitModule("c", CMethods);
    PyModule_AddStringConstant(module, "__version__", FULL_VERSION);
}
