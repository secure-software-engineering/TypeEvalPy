# Functions are assigned to variables via starred assignment
def func1():
    return [72, 72, 30]


def func2():
    return (27, 21, 38)


def func3():
    return {'bhcbl': 43, 'eugps': 93, 'amabs': 78}


def func4():
    return 63.21

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
