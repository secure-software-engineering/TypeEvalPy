# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return 'acxgx'


def func3():
    return (83, 13, 63)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 61


b = ["Hello"]
b[0] = func4

f = b[0]()
