# Functions are assigned to variables via starred assignment
def func1():
    return [3, 41, 84]


def func2():
    return 'ktwar'


def func3():
    return {'dqixx': 54, 'svqbj': 72, 'jpprz': 39}


def func4():
    return 67

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
