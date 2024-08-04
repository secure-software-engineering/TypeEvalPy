# Functions are assigned to variables via starred assignment
def func1():
    return [76, 35, 82]


def func2():
    return 99.77


def func3():
    return (7, 35, 20)


def func4():
    return {'dqrhi': 99, 'hcqjj': 67, 'cinvy': 10}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
