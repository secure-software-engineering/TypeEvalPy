# Functions are assigned as elements of a list and then called.


def func1():
    return 'mvkmi'


def func2():
    return 3


def func3():
    return {'csfjl': 69, 'rbzmz': 54, 'yvint': 50}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (4, 34, 72)


b = ["Hello"]
b[0] = func4

f = b[0]()