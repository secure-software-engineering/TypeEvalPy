# A function `func` is defined which takes as a parameter a variable which has a function assigned to it which it later calls.


def param_func():
    return "Hello from param_func"


def func(a):
    return a()


b = param_func
c = func(b)
