# Functions are assigned to variables via starred assignment
def func1():
    return 'szsfd'


def func2():
    return (12, 45, 50)


def func3():
    return 3


def func4():
    return [44, 38, 21]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
