# Functions are assigned to variables via starred assignment
def func1():
    return (19, 68, 51)


def func2():
    return {'surxl': 69, 'tgoqn': 68, 'ewehp': 60}


def func3():
    return 'wotcp'


def func4():
    return [83, 39, 10]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
