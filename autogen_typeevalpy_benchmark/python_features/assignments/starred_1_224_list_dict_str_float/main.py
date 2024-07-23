# Functions are assigned to variables via starred assignment
def func1():
    return [16, 67, 46]


def func2():
    return {'jqged': 100, 'algme': 38, 'jjval': 18}


def func3():
    return 'imbqa'


def func4():
    return 87.54

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
