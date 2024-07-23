# Functions are assigned to variables via starred assignment
def func1():
    return 'ufowe'


def func2():
    return 97.32


def func3():
    return {'zpvag': 77, 'yxpir': 32, 'ytzzk': 47}


def func4():
    return (16, 2, 67)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
