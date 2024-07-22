# Functions are assigned to variables via starred assignment
def func1():
    return 82


def func2():
    return 'kwekw'


def func3():
    return [20, 37, 70]


def func4():
    return {'cfsmo': 68, 'tgivf': 20, 'qjxdd': 12}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
