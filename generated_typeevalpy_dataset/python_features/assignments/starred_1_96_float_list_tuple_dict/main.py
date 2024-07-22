# Functions are assigned to variables via starred assignment
def func1():
    return 6.29


def func2():
    return [80, 83, 17]


def func3():
    return (82, 80, 99)


def func4():
    return {'oaajc': 40, 'qmdtg': 82, 'ljxht': 46}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
