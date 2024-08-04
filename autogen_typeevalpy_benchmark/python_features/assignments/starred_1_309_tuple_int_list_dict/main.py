# Functions are assigned to variables via starred assignment
def func1():
    return (81, 52, 63)


def func2():
    return 7


def func3():
    return [39, 92, 90]


def func4():
    return {'zxcwf': 27, 'ooqxu': 21, 'mavag': 3}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
