# Functions are assigned to variables via starred assignment
def func1():
    return (47, 56, 2)


def func2():
    return 39


def func3():
    return {'kqiyi': 50, 'arhdt': 45, 'gdbyt': 29}


def func4():
    return 87.34

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
