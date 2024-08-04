# Functions are assigned to variables via starred assignment
def func1():
    return {'fenbu': 78, 'eirpy': 46, 'mflxo': 63}


def func2():
    return 75


def func3():
    return 'ijoqd'


def func4():
    return [93, 58, 35]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
