# Functions are assigned to variables via starred assignment
def func1():
    return 37


def func2():
    return [70, 62, 30]


def func3():
    return 'chpek'


def func4():
    return {'rdwej': 4, 'twfpf': 7, 'pixfa': 38}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
