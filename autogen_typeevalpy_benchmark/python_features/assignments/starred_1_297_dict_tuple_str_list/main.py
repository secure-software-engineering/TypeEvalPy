# Functions are assigned to variables via starred assignment
def func1():
    return {'hrifp': 48, 'gtmil': 99, 'lhkav': 57}


def func2():
    return (39, 4, 26)


def func3():
    return 'alamr'


def func4():
    return [40, 87, 73]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
