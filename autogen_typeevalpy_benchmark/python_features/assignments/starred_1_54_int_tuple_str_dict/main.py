# Functions are assigned to variables via starred assignment
def func1():
    return 70


def func2():
    return (19, 17, 87)


def func3():
    return 'skfuy'


def func4():
    return {'yfuvn': 52, 'oyiiy': 39, 'rqbjv': 47}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
