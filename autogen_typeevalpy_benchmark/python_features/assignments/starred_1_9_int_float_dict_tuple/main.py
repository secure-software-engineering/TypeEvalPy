# Functions are assigned to variables via starred assignment
def func1():
    return 79


def func2():
    return 39.71


def func3():
    return {'ujzcs': 81, 'tfvls': 82, 'rkwhn': 2}


def func4():
    return (48, 36, 94)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
