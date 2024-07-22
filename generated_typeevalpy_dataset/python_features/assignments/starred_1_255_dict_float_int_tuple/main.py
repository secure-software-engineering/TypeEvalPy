# Functions are assigned to variables via starred assignment
def func1():
    return {'sgpiw': 83, 'wqiuu': 54, 'edydt': 93}


def func2():
    return 20.61


def func3():
    return 12


def func4():
    return (54, 59, 90)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
