# Functions are assigned to variables via starred assignment
def func1():
    return {'hksga': 63, 'gjvii': 99, 'dkslm': 69}


def func2():
    return 'prxfq'


def func3():
    return 63


def func4():
    return (53, 25, 74)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
