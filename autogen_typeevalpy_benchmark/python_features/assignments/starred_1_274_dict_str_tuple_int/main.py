# Functions are assigned to variables via starred assignment
def func1():
    return {'yumrd': 49, 'mlpsk': 63, 'lkiwf': 3}


def func2():
    return 'dhsza'


def func3():
    return (48, 24, 2)


def func4():
    return 85

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
