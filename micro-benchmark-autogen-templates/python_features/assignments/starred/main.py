# Functions are assigned to variables via starred assignment
def func1():
    return <value1>


def func2():
    return <value2>


def func3():
    return <value3>


def func4():
    return <value4>

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
