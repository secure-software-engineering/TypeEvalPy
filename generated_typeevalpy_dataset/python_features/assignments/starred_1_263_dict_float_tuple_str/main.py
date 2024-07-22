# Functions are assigned to variables via starred assignment
def func1():
    return {'gdgwn': 61, 'sqstm': 33, 'tekdq': 76}


def func2():
    return 66.64


def func3():
    return (41, 67, 32)


def func4():
    return 'pasng'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
