# Functions are assigned to variables via starred assignment
def func1():
    return [55, 27, 33]


def func2():
    return 'bjtof'


def func3():
    return 26.53


def func4():
    return (19, 86, 81)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
