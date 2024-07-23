# Functions are assigned to variables via starred assignment
def func1():
    return [2, 40, 15]


def func2():
    return {'vftuo': 59, 'aptpl': 73, 'oriay': 54}


def func3():
    return 14


def func4():
    return 69.69

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
