# Functions are assigned to variables via starred assignment
def func1():
    return 36


def func2():
    return 'fygbo'


def func3():
    return {'jrtzy': 86, 'jxcsr': 87, 'kwajg': 24}


def func4():
    return [93, 87, 61]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
