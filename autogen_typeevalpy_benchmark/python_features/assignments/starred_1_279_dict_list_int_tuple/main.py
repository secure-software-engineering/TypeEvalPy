# Functions are assigned to variables via starred assignment
def func1():
    return {'fwxjv': 67, 'cmlru': 95, 'ssxya': 64}


def func2():
    return [97, 84, 37]


def func3():
    return 21


def func4():
    return (78, 33, 1)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
