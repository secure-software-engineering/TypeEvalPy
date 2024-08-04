# Functions are assigned to variables via starred assignment
def func1():
    return 81.98


def func2():
    return 'ttcpp'


def func3():
    return [28, 63, 72]


def func4():
    return (65, 10, 12)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
