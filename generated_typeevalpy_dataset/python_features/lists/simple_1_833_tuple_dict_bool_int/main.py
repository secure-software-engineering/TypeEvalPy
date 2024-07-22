# Functions are assigned as elements of a list and then called.


def func1():
    return (25, 96, 32)


def func2():
    return {'uxteb': 22, 'irmnw': 82, 'imekv': 14}


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 99


b = ["Hello"]
b[0] = func4

f = b[0]()
