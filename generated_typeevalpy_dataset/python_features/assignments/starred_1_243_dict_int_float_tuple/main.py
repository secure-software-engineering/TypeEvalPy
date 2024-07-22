# Functions are assigned to variables via starred assignment
def func1():
    return {'acyev': 54, 'pptvt': 62, 'oczmj': 10}


def func2():
    return 18


def func3():
    return 67.53


def func4():
    return (69, 53, 83)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
