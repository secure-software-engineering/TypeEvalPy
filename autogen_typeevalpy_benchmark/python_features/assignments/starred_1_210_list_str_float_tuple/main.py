# Functions are assigned to variables via starred assignment
def func1():
    return [69, 77, 27]


def func2():
    return 'auxrk'


def func3():
    return 25.06


def func4():
    return (67, 15, 53)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
