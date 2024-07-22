# Functions are assigned to variables via starred assignment
def func1():
    return 9


def func2():
    return (98, 21, 64)


def func3():
    return [37, 49, 30]


def func4():
    return {'utjzt': 39, 'irqwq': 36, 'pjlak': 40}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
