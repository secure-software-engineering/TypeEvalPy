# Functions are assigned to variables via starred assignment
def func1():
    return 'xkaws'


def func2():
    return {'goigl': 44, 'iwjpi': 43, 'arqpx': 94}


def func3():
    return [51, 70, 23]


def func4():
    return 36.88

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
