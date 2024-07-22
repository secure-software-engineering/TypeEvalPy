# Functions are assigned to variables via starred assignment
def func1():
    return (88, 53, 92)


def func2():
    return {'rqbiz': 100, 'thxgc': 56, 'glcss': 61}


def func3():
    return 52.86


def func4():
    return 'zzexd'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
