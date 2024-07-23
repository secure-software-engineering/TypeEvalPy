# Functions are assigned to variables via starred assignment
def func1():
    return {'ztchy': 26, 'zidzc': 15, 'hhobt': 46}


def func2():
    return 50.54


def func3():
    return [91, 36, 92]


def func4():
    return 54

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
