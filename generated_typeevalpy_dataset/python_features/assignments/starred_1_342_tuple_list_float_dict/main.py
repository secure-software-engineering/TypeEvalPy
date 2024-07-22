# Functions are assigned to variables via starred assignment
def func1():
    return (50, 73, 73)


def func2():
    return [83, 99, 3]


def func3():
    return 61.73


def func4():
    return {'lrmyw': 11, 'zxzis': 62, 'jaqkq': 83}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
