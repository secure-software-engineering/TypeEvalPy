# Functions are assigned as elements of a list and then called.


def func1():
    return 12.75


def func2():
    return 76


def func3():
    return [48, 41, 1]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'tqpmx'


b = ["Hello"]
b[0] = func4

f = b[0]()
