# Functions are assigned to variables via starred assignment
def func1():
    return {'zyqnb': 83, 'asbzl': 72, 'cfwtv': 99}


def func2():
    return (49, 43, 91)


def func3():
    return [15, 48, 91]


def func4():
    return 79.94

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
