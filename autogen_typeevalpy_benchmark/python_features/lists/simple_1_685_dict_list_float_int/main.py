# Functions are assigned as elements of a list and then called.


def func1():
    return {'mgnlm': 95, 'wwgni': 97, 'nwjlh': 44}


def func2():
    return [100, 45, 33]


def func3():
    return 17.21


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 32


b = ["Hello"]
b[0] = func4

f = b[0]()
