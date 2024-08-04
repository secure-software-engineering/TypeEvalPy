# Functions are assigned to variables via starred assignment
def func1():
    return (33, 45, 22)


def func2():
    return [48, 57, 29]


def func3():
    return 24.91


def func4():
    return {'psazt': 62, 'vubji': 48, 'liqhk': 16}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
