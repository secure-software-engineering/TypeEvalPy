# This program demonstrates the use of functions as objects and parameters in Python.
# A function `func` is defined which takes a function as a parameter and calls it.
# A function `func2` is defined which returns another function `func3`.
# A function `func3` is defined which does nothing but returns a string value.
# The `func` function is called with the return value of `func2` as the argument.


def func(a):
    return a()


def func2():
    return func3


def func3():
    return 44.57


b = func(func2())
