# Functions are assigned to variables via starred assignment
def func1():
    return 'qmwtp'


def func2():
    return [34, 31, 85]


def func3():
    return 8.1


def func4():
    return {'xgndj': 43, 'jzigf': 84, 'hzqik': 48}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
