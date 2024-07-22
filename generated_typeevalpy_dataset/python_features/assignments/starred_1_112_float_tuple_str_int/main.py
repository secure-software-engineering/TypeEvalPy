# Functions are assigned to variables via starred assignment
def func1():
    return 89.42


def func2():
    return (84, 41, 81)


def func3():
    return 'dtpqg'


def func4():
    return 17

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
