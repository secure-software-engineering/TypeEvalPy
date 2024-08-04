# Functions are assigned to variables via starred assignment
def func1():
    return [89, 40, 79]


def func2():
    return 'yyzqw'


def func3():
    return 15


def func4():
    return {'imtjy': 16, 'xkuen': 96, 'qzkau': 53}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
