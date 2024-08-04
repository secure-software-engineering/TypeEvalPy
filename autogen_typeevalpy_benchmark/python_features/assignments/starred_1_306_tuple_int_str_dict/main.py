# Functions are assigned to variables via starred assignment
def func1():
    return (15, 99, 15)


def func2():
    return 20


def func3():
    return 'aecsf'


def func4():
    return {'cfcph': 21, 'aqybo': 25, 'nbjkv': 15}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
