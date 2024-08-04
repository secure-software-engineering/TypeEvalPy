# Functions are assigned to variables via starred assignment
def func1():
    return 'xbxmg'


def func2():
    return 75.03


def func3():
    return {'zqddq': 53, 'tksuq': 57, 'bpdnz': 95}


def func4():
    return (81, 88, 20)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
