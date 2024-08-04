# Functions are assigned to variables via starred assignment
def func1():
    return (18, 20, 64)


def func2():
    return 77.77


def func3():
    return {'yzjpx': 85, 'rrqst': 8, 'tuknn': 75}


def func4():
    return 'irlzp'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
