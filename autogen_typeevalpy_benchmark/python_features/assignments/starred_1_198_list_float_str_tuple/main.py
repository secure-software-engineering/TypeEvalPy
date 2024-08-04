# Functions are assigned to variables via starred assignment
def func1():
    return [94, 100, 31]


def func2():
    return 40.87


def func3():
    return 'asdoo'


def func4():
    return (91, 82, 8)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
