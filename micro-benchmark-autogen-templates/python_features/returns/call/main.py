# A function `func` is called and returns a function `return_func` which is later called, via a variable.


def return_func():
    return <value1>


def func():
    return return_func


a = func()
b = a()
