# Functions are assigned to variables via starred assignment
def func1():
    return 50.68


def func2():
    return {'pkico': 12, 'rifzu': 66, 'hlihl': 83}


def func3():
    return (98, 83, 53)


def func4():
    return [66, 63, 86]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
