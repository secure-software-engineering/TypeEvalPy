# Functions are assigned to variables via starred assignment
def func1():
    return [56, 15, 84]


def func2():
    return (43, 38, 94)


def func3():
    return 53


def func4():
    return {'kpncd': 3, 'kqmfb': 19, 'xwwoz': 2}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
