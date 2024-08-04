# Functions are assigned to variables via starred assignment
def func1():
    return 'ckpzq'


def func2():
    return [13, 33, 94]


def func3():
    return {'zrmvv': 99, 'ghoso': 52, 'znfyj': 5}


def func4():
    return 13.14

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
