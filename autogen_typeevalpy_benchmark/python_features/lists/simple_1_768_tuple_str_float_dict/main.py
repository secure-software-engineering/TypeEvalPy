# Functions are assigned as elements of a list and then called.


def func1():
    return (80, 6, 90)


def func2():
    return 'olfqv'


def func3():
    return 22.16


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'nasxz': 84, 'xhjan': 70, 'pkkws': 98}


b = ["Hello"]
b[0] = func4

f = b[0]()
