# Functions are assigned to variables via starred assignment
def func1():
    return (47, 59, 9)


def func2():
    return 'kkvnz'


def func3():
    return {'taart': 94, 'atpzl': 54, 'vmunn': 92}


def func4():
    return [91, 98, 56]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
