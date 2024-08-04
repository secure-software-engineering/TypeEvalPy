# Functions are assigned to variables via starred assignment
def func1():
    return 83


def func2():
    return {'thyyj': 29, 'kumbj': 33, 'xujhy': 43}


def func3():
    return 'shrxz'


def func4():
    return (85, 54, 46)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
