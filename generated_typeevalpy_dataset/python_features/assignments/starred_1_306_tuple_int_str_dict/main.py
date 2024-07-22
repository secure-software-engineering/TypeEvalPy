# Functions are assigned to variables via starred assignment
def func1():
    return (71, 79, 35)


def func2():
    return 55


def func3():
    return 'tfqxa'


def func4():
    return {'izogz': 85, 'dqyml': 89, 'tpydj': 99}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
