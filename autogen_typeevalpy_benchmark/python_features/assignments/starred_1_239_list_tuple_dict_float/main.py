# Functions are assigned to variables via starred assignment
def func1():
    return [18, 84, 98]


def func2():
    return (25, 68, 39)


def func3():
    return {'rjobr': 16, 'yxvwm': 64, 'fybgg': 87}


def func4():
    return 89.01

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
