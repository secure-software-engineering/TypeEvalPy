# Functions are assigned to variables via starred assignment
def func1():
    return [75, 27, 53]


def func2():
    return 1.87


def func3():
    return 62


def func4():
    return {'dqfwe': 76, 'hipau': 70, 'hqghd': 35}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
