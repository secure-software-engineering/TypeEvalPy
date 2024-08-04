# Functions are assigned to variables via starred assignment
def func1():
    return {'hlwkw': 7, 'ucqfs': 51, 'mwomt': 54}


def func2():
    return [10, 41, 90]


def func3():
    return (39, 45, 80)


def func4():
    return 'wikgl'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
