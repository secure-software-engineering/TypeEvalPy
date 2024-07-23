# Functions are assigned to variables via starred assignment
def func1():
    return 'jsvti'


def func2():
    return 40.68


def func3():
    return {'htlwb': 31, 'khvjx': 96, 'qyenw': 77}


def func4():
    return 72

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
