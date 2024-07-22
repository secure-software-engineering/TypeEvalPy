# Functions are assigned to variables via starred assignment
def func1():
    return [69, 34, 51]


def func2():
    return 44


def func3():
    return {'nsgdn': 29, 'xawri': 81, 'daexd': 15}


def func4():
    return 'mzycw'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
