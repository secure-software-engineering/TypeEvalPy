# Functions are assigned to variables via starred assignment
def func1():
    return {'himub': 18, 'ldpnl': 66, 'xoenu': 19}


def func2():
    return 'xrbqj'


def func3():
    return [16, 57, 4]


def func4():
    return (1, 44, 26)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
