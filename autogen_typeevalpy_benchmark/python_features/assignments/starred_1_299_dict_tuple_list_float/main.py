# Functions are assigned to variables via starred assignment
def func1():
    return {'xoqyr': 100, 'dwxdy': 98, 'yxuqn': 10}


def func2():
    return (51, 84, 41)


def func3():
    return [13, 9, 79]


def func4():
    return 63.29

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
