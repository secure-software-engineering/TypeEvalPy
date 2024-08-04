# Functions are assigned to variables via starred assignment
def func1():
    return 'nfuzf'


def func2():
    return [45, 14, 97]


def func3():
    return (25, 79, 1)


def func4():
    return {'bepxi': 99, 'miplw': 9, 'xissk': 89}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
