# A function `func` is called and returns a function `return_func` which is later called, via a variable.


def return_func():
    return 57.12


def func():
    return return_func


a = func()
b = a()
