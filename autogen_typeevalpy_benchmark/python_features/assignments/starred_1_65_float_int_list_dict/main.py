# Functions are assigned to variables via starred assignment
def func1():
    return 21.26


def func2():
    return 16


def func3():
    return [29, 89, 46]


def func4():
    return {'mnivs': 75, 'luhfd': 80, 'lxmph': 78}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
