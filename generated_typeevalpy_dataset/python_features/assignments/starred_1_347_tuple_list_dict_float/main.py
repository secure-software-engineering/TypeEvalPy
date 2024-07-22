# Functions are assigned to variables via starred assignment
def func1():
    return (57, 84, 85)


def func2():
    return [84, 77, 53]


def func3():
    return {'ajkfo': 45, 'iksgd': 7, 'deipq': 85}


def func4():
    return 69.59

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
