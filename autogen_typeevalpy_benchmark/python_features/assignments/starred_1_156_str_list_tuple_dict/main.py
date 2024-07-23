# Functions are assigned to variables via starred assignment
def func1():
    return 'mxhvg'


def func2():
    return [30, 22, 52]


def func3():
    return (99, 77, 10)


def func4():
    return {'safsm': 35, 'astvg': 76, 'ulime': 93}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
