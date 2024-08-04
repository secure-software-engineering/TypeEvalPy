# Functions are assigned to variables via starred assignment
def func1():
    return (71, 25, 57)


def func2():
    return {'oxtlp': 65, 'xoglg': 6, 'gbvnq': 51}


def func3():
    return 'eidbw'


def func4():
    return 64.85

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
