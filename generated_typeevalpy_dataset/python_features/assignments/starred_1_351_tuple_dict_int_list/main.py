# Functions are assigned to variables via starred assignment
def func1():
    return (91, 9, 16)


def func2():
    return {'yvpbu': 11, 'vbhin': 61, 'xgjac': 36}


def func3():
    return 26


def func4():
    return [14, 97, 80]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
