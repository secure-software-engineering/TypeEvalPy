# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return 24.58


def func3():
    return 54


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ytinq': 47, 'ldxir': 23, 'wjmnc': 83}


b = ["Hello"]
b[0] = func4

f = b[0]()
