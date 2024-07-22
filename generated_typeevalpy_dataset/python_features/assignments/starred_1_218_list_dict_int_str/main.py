# Functions are assigned to variables via starred assignment
def func1():
    return [85, 57, 3]


def func2():
    return {'gglia': 9, 'sauue': 74, 'ojknq': 1}


def func3():
    return 21


def func4():
    return 'aqsvo'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
