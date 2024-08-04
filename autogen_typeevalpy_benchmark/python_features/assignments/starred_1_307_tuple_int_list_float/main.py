# Functions are assigned to variables via starred assignment
def func1():
    return (74, 14, 87)


def func2():
    return 74


def func3():
    return [76, 5, 66]


def func4():
    return 16.25

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
