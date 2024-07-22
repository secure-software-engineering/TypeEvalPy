# Functions are assigned to variables via starred assignment
def func1():
    return 'cswig'


def func2():
    return [48, 40, 35]


def func3():
    return {'lteyf': 88, 'eosgh': 19, 'sxvzh': 72}


def func4():
    return 47.55

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
