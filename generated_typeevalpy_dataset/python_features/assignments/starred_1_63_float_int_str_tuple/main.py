# Functions are assigned to variables via starred assignment
def func1():
    return 76.84


def func2():
    return 39


def func3():
    return 'ldwzv'


def func4():
    return (98, 61, 94)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
