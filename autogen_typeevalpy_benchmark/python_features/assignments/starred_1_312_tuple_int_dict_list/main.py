# Functions are assigned to variables via starred assignment
def func1():
    return (86, 5, 18)


def func2():
    return 63


def func3():
    return {'inare': 44, 'anxqf': 16, 'ukzbd': 75}


def func4():
    return [62, 26, 83]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
