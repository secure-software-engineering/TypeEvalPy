# Functions are assigned to variables via starred assignment
def func1():
    return {'ggyrz': 71, 'wrcgu': 75, 'femzf': 33}


def func2():
    return (70, 16, 12)


def func3():
    return 40


def func4():
    return 53.65

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
