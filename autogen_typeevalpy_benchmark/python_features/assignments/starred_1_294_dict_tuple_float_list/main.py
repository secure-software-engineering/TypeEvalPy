# Functions are assigned to variables via starred assignment
def func1():
    return {'xxkqe': 74, 'rolil': 8, 'brmlh': 4}


def func2():
    return (72, 31, 68)


def func3():
    return 90.23


def func4():
    return [24, 91, 94]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
