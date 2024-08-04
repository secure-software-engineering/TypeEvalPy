# Functions are assigned to variables via starred assignment
def func1():
    return 95


def func2():
    return {'niyxy': 46, 'hucyk': 51, 'mpoyd': 45}


def func3():
    return 80.34


def func4():
    return [69, 69, 57]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
