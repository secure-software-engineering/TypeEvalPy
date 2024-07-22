# Functions are assigned to variables via starred assignment
def func1():
    return (69, 32, 83)


def func2():
    return 'jzljb'


def func3():
    return {'yqjrk': 25, 'hpdla': 20, 'eegfi': 77}


def func4():
    return 54

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
