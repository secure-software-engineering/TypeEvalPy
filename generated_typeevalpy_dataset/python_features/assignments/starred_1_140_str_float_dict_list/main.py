# Functions are assigned to variables via starred assignment
def func1():
    return 'iqkag'


def func2():
    return 4.54


def func3():
    return {'xpeyt': 61, 'cjcrc': 10, 'qwpix': 33}


def func4():
    return [64, 77, 24]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
