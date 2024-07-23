# Functions are assigned to variables via starred assignment
def func1():
    return {'xmvdw': 9, 'nqoza': 11, 'kwtdd': 21}


def func2():
    return (12, 60, 34)


def func3():
    return [49, 81, 77]


def func4():
    return 'xmqyi'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
