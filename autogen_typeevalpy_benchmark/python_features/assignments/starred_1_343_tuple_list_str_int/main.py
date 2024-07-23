# Functions are assigned to variables via starred assignment
def func1():
    return (88, 41, 52)


def func2():
    return [100, 9, 41]


def func3():
    return 'evfou'


def func4():
    return 67

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
