# Functions are assigned to variables via starred assignment
def func1():
    return [44, 88, 11]


def func2():
    return 20


def func3():
    return 93.96


def func4():
    return {'destc': 35, 'xjjhk': 52, 'nqrsb': 54}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
