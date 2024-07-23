# Functions are assigned as elements of a list and then called.


def func1():
    return {'hornv': 15, 'wydff': 12, 'ytvbe': 10}


def func2():
    return 89.48


def func3():
    return 64


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
