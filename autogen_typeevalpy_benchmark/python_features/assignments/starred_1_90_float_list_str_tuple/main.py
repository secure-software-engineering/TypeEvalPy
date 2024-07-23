# Functions are assigned to variables via starred assignment
def func1():
    return 87.03


def func2():
    return [19, 19, 26]


def func3():
    return 'kkhpa'


def func4():
    return (26, 18, 84)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
