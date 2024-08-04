# Functions are assigned as elements of a list and then called.


def func1():
    return (70, 33, 61)


def func2():
    return 16.58


def func3():
    return {'lkgxe': 72, 'omccz': 25, 'pvhiq': 75}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [49, 28, 23]


b = ["Hello"]
b[0] = func4

f = b[0]()
