# Functions are assigned to variables via starred assignment
def func1():
    return 'vkeat'


def func2():
    return 33.4


def func3():
    return {'mqehd': 33, 'hothr': 56, 'ejoon': 84}


def func4():
    return 89

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
