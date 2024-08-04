# Functions are assigned to variables via starred assignment
def func1():
    return {'uzjwl': 40, 'txmkz': 87, 'ojnzf': 5}


def func2():
    return 49.39


def func3():
    return (89, 27, 8)


def func4():
    return 57

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
