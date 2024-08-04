# Functions are assigned as elements of a list and then called.


def func1():
    return (61, 44, 2)


def func2():
    return 100


def func3():
    return 'tpbmf'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [94, 54, 25]


b = ["Hello"]
b[0] = func4

f = b[0]()
