# Functions are assigned to variables via starred assignment
def func1():
    return 61.88


def func2():
    return {'pqweg': 28, 'hbyeo': 57, 'atcgq': 93}


def func3():
    return (39, 71, 96)


def func4():
    return [19, 31, 69]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
