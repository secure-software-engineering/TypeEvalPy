# Functions are assigned as elements of a list and then called.


def func1():
    return [29, 41, 64]


def func2():
    return 10.86


def func3():
    return 'ftnmp'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
