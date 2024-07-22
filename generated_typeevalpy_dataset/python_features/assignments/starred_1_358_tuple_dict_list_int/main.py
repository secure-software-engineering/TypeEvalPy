# Functions are assigned to variables via starred assignment
def func1():
    return (80, 58, 63)


def func2():
    return {'fjzxg': 1, 'tmtub': 83, 'megzm': 40}


def func3():
    return [92, 49, 22]


def func4():
    return 82

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
