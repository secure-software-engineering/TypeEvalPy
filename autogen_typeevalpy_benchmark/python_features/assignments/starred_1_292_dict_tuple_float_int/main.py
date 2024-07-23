# Functions are assigned to variables via starred assignment
def func1():
    return {'fstoj': 3, 'mmtvw': 12, 'modhi': 43}


def func2():
    return (24, 56, 32)


def func3():
    return 34.9


def func4():
    return 63

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
