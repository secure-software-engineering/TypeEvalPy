# Functions are assigned to variables via starred assignment
def func1():
    return (93, 19, 79)


def func2():
    return 'zbhvk'


def func3():
    return 71.24


def func4():
    return [75, 33, 82]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
