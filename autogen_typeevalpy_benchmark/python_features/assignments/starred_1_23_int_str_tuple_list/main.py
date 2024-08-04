# Functions are assigned to variables via starred assignment
def func1():
    return 91


def func2():
    return 'aasmg'


def func3():
    return (7, 98, 15)


def func4():
    return [43, 64, 82]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
