# Functions are assigned to variables via starred assignment
def func1():
    return {'vxwjy': 21, 'pakwx': 18, 'iyzah': 12}


def func2():
    return 47


def func3():
    return (96, 8, 2)


def func4():
    return [66, 47, 21]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
