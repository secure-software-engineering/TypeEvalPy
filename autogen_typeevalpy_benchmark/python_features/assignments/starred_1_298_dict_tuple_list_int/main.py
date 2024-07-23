# Functions are assigned to variables via starred assignment
def func1():
    return {'tdhct': 10, 'cqrxw': 73, 'udxqj': 66}


def func2():
    return (16, 18, 49)


def func3():
    return [32, 30, 18]


def func4():
    return 80

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
