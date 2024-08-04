# Functions are assigned to variables via starred assignment
def func1():
    return 76


def func2():
    return (4, 96, 37)


def func3():
    return [81, 34, 25]


def func4():
    return {'xnsqg': 83, 'wjxca': 14, 'qezmd': 42}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
