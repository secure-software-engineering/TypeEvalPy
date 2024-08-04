# Functions are assigned to variables via starred assignment
def func1():
    return 66


def func2():
    return {'ftgfh': 51, 'tfyjo': 39, 'lekml': 67}


def func3():
    return [41, 31, 20]


def func4():
    return 3.9

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
