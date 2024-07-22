# Functions are assigned to variables via starred assignment
def func1():
    return 83


def func2():
    return [34, 54, 40]


def func3():
    return 'nqadx'


def func4():
    return {'ubfsf': 18, 'pzisi': 55, 'gljhy': 48}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
