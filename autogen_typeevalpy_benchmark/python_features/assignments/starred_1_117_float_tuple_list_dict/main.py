# Functions are assigned to variables via starred assignment
def func1():
    return 19.69


def func2():
    return (92, 34, 10)


def func3():
    return [30, 69, 55]


def func4():
    return {'ikjut': 32, 'tfbeh': 23, 'zugbc': 70}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
