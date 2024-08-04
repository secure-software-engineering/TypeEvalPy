# Functions are assigned to variables via starred assignment
def func1():
    return 'ukzqe'


def func2():
    return (26, 21, 30)


def func3():
    return [25, 88, 100]


def func4():
    return 24.94

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
