# Functions are assigned as elements of a list and then called.


def func1():
    return (36, 16, 24)


def func2():
    return {'hdqwq': 14, 'iranq': 52, 'xhjnt': 89}


def func3():
    return 50.54


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [67, 18, 53]


b = ["Hello"]
b[0] = func4

f = b[0]()
