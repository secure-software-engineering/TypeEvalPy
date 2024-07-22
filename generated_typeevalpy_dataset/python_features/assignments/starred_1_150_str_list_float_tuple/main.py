# Functions are assigned to variables via starred assignment
def func1():
    return 'rtflg'


def func2():
    return [93, 50, 36]


def func3():
    return 26.11


def func4():
    return (29, 53, 26)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
