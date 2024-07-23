# Functions are assigned to variables via starred assignment
def func1():
    return [39, 26, 75]


def func2():
    return (12, 75, 100)


def func3():
    return 'tdzny'


def func4():
    return {'xszre': 51, 'kdhbm': 54, 'bjsnd': 48}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
