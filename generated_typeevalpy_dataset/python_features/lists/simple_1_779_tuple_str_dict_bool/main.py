# Functions are assigned as elements of a list and then called.


def func1():
    return (25, 94, 79)


def func2():
    return 'nlbse'


def func3():
    return {'fmyzp': 36, 'rbgds': 68, 'roumr': 2}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
