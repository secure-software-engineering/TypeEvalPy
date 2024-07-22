# Functions are assigned to variables via starred assignment
def func1():
    return 'mjadd'


def func2():
    return {'krzws': 60, 'txklh': 34, 'pwpuq': 84}


def func3():
    return (29, 49, 73)


def func4():
    return [40, 47, 18]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
