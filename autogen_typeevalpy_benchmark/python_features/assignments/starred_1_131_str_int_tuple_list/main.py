# Functions are assigned to variables via starred assignment
def func1():
    return 'geshb'


def func2():
    return 92


def func3():
    return (97, 16, 34)


def func4():
    return [59, 73, 94]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
