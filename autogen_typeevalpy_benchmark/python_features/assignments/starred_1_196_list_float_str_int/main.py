# Functions are assigned to variables via starred assignment
def func1():
    return [54, 74, 2]


def func2():
    return 88.0


def func3():
    return 'qndpf'


def func4():
    return 43

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
