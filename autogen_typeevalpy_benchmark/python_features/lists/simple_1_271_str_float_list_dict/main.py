# Functions are assigned as elements of a list and then called.


def func1():
    return 'yyfww'


def func2():
    return 23.4


def func3():
    return [77, 64, 49]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'evhqv': 24, 'zfjhj': 25, 'otsnp': 79}


b = ["Hello"]
b[0] = func4

f = b[0]()
