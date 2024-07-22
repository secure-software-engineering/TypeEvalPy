# Functions are assigned to variables via starred assignment
def func1():
    return 'ztcuy'


def func2():
    return 59


def func3():
    return {'ycqov': 33, 'rmqlg': 74, 'ntsqa': 82}


def func4():
    return [45, 11, 47]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
