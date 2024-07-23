# Functions are assigned to variables via starred assignment
def func1():
    return {'jadpg': 72, 'emyhb': 24, 'rcbwd': 83}


def func2():
    return 'sfiij'


def func3():
    return 10.89


def func4():
    return (15, 79, 59)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
