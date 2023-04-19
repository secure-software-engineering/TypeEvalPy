# A variable is assigned a function repeatedly.


def func1():
    return 42


def func2():
    return "Hello from func2"


a = func1

b = a()

a = func2

b = a()

a = func1

b = a()

a = func2

b = a()
