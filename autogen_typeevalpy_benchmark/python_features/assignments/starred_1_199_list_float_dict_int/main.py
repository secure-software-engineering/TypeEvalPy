# Functions are assigned to variables via starred assignment
def func1():
    return [39, 89, 58]


def func2():
    return 67.8


def func3():
    return {'msgdu': 54, 'ztmly': 63, 'bpflb': 65}


def func4():
    return 80

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
