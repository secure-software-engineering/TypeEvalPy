# Functions are assigned to variables via starred assignment
def func1():
    return {'jzmya': 19, 'whvvn': 9, 'wmuws': 98}


def func2():
    return [37, 61, 88]


def func3():
    return 'gshha'


def func4():
    return 23

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
