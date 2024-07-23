# Functions are assigned to variables via starred assignment
def func1():
    return 'cixjy'


def func2():
    return (35, 66, 1)


def func3():
    return 46.68


def func4():
    return [75, 77, 29]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
