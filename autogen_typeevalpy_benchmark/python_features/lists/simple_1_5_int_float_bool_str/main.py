# Functions are assigned as elements of a list and then called.


def func1():
    return 17


def func2():
    return 48.81


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'gkorx'


b = ["Hello"]
b[0] = func4

f = b[0]()
