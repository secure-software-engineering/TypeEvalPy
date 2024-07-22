# Functions are assigned to variables via starred assignment
def func1():
    return (89, 50, 53)


def func2():
    return {'qznpb': 99, 'yozbr': 73, 'rayhy': 42}


def func3():
    return 82.79


def func4():
    return [18, 13, 26]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
