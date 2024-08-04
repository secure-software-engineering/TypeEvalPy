# Functions are assigned to variables via starred assignment
def func1():
    return 72


def func2():
    return 98.55


def func3():
    return {'xhsbw': 14, 'dqtco': 43, 'fbqxa': 38}


def func4():
    return [51, 15, 61]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
