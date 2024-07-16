# Functions are assigned as elements of a list and then called.


def func1():
    return <value1>


def func2():
    return <value2>


def func3():
    return <value3>


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return <value4>


b = []
b[0] = func4

f = b[0]()
