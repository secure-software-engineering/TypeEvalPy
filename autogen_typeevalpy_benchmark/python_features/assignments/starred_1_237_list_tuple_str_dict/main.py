# Functions are assigned to variables via starred assignment
def func1():
    return [38, 85, 81]


def func2():
    return (83, 42, 47)


def func3():
    return 'mwgsg'


def func4():
    return {'dszsz': 7, 'ktzjd': 1, 'vqiqe': 7}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
