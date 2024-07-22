# Functions are assigned to variables via starred assignment
def func1():
    return {'vmyyv': 69, 'ngbnj': 61, 'avxbw': 77}


def func2():
    return 51


def func3():
    return (48, 73, 58)


def func4():
    return [42, 13, 76]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
