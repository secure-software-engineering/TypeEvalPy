# Functions are assigned to variables via starred assignment
def func1():
    return (99, 88, 80)


def func2():
    return 56


def func3():
    return 'rxlke'


def func4():
    return [31, 38, 17]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
