# Functions are assigned to variables via starred assignment
def func1():
    return {'jspxj': 73, 'mopjj': 91, 'xiqrk': 81}


def func2():
    return (11, 57, 15)


def func3():
    return [39, 66, 47]


def func4():
    return 37

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
