# Functions are assigned to variables via starred assignment
def func1():
    return 'yjwta'


def func2():
    return (56, 49, 93)


def func3():
    return 59.42


def func4():
    return [77, 24, 84]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
