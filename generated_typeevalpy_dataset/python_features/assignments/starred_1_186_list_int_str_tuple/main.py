# Functions are assigned to variables via starred assignment
def func1():
    return [1, 12, 94]


def func2():
    return 23


def func3():
    return 'vcqzk'


def func4():
    return (22, 45, 66)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
