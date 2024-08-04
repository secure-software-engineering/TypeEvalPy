# Functions are assigned to variables via starred assignment
def func1():
    return [14, 62, 100]


def func2():
    return (88, 4, 28)


def func3():
    return 94


def func4():
    return {'ggayb': 83, 'qupkk': 59, 'jssyp': 31}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
