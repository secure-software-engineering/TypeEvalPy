# Functions are assigned to variables via starred assignment
def func1():
    return [66, 61, 91]


def func2():
    return 'njnry'


def func3():
    return {'ybjap': 1, 'ikotj': 93, 'eamem': 82}


def func4():
    return 71

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
