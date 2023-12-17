# Lists containing lists that contain functions.


def func1():
    return 42


def func2():
    return "Hello from func2"


ls = [[func1], func2]

a = ls[0]
b = a[0]
c = b()
