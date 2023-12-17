# Functions are assigned as elements of a list and then called.


def func1():
    return 42


def func2():
    return 42.5


def func3():
    return "Hello from func3"


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = []
b[0] = func4

f = b[0]()
