# Functions are assigned to variables via starred assignment
def func1():
    return 36.18


def func2():
    return (48, 26, 35)


def func3():
    return [54, 99, 41]


def func4():
    return 'ncfqn'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
