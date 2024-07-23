# Functions are assigned as elements of a list and then called.


def func1():
    return (24, 86, 43)


def func2():
    return [69, 48, 86]


def func3():
    return 9.19


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ydjut': 26, 'igrzr': 32, 'zhdcd': 74}


b = ["Hello"]
b[0] = func4

f = b[0]()
