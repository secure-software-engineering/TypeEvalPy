# Functions are assigned to variables via starred assignment
def func1():
    return {'lqixu': 17, 'boadv': 82, 'fhvil': 84}


def func2():
    return (58, 63, 22)


def func3():
    return 'nlzyj'


def func4():
    return [56, 85, 80]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
