# Functions are assigned to variables via starred assignment
def func1():
    return (100, 30, 64)


def func2():
    return 45.76


def func3():
    return {'zufwr': 12, 'qizwj': 77, 'klazw': 53}


def func4():
    return 83

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
