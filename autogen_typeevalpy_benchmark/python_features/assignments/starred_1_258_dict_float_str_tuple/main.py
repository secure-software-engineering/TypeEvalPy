# Functions are assigned to variables via starred assignment
def func1():
    return {'rqxps': 74, 'azmkc': 77, 'dgvpq': 17}


def func2():
    return 47.19


def func3():
    return 'qysyx'


def func4():
    return (29, 28, 67)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
