# A function is defined, assigned to a variable and called via that variable.


def func():
    return "Hello from func"


a = func
b = a()
