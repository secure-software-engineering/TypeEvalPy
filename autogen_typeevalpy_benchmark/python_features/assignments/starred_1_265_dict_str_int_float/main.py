# Functions are assigned to variables via starred assignment
def func1():
    return {'fdkiw': 29, 'owonm': 85, 'shmjv': 8}


def func2():
    return 'hdhlo'


def func3():
    return 45


def func4():
    return 97.49

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
