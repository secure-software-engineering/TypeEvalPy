# Functions are assigned as elements of a list and then called.


def func1():
    return 64


def func2():
    return (7, 15, 71)


def func3():
    return {'mvtoh': 58, 'rkzax': 54, 'fsnzj': 22}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
