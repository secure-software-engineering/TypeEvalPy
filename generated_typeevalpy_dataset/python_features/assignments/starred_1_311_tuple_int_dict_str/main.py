# Functions are assigned to variables via starred assignment
def func1():
    return (5, 47, 83)


def func2():
    return 70


def func3():
    return {'jayce': 33, 'mydmx': 88, 'qkzbs': 93}


def func4():
    return 'xmpon'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
