# Functions are assigned to variables via starred assignment
def func1():
    return 'seinx'


def func2():
    return {'xhdxs': 34, 'ackog': 15, 'qoigk': 97}


def func3():
    return (72, 59, 98)


def func4():
    return 83.44

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
