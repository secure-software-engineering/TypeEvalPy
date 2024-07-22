# Functions are assigned to variables via starred assignment
def func1():
    return [19, 75, 13]


def func2():
    return {'mpjdd': 82, 'hihyu': 44, 'fnbsk': 29}


def func3():
    return 24.95


def func4():
    return 'myofm'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
