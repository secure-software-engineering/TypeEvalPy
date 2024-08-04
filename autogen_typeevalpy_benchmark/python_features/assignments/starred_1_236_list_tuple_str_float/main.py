# Functions are assigned to variables via starred assignment
def func1():
    return [72, 79, 25]


def func2():
    return (48, 97, 34)


def func3():
    return 'kkvnp'


def func4():
    return 2.54

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
