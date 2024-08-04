# Functions are assigned to variables via starred assignment
def func1():
    return 22


def func2():
    return {'expxn': 56, 'pmpgi': 42, 'ndimm': 78}


def func3():
    return 83.76


def func4():
    return 'javxj'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
