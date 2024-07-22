# Functions are assigned as elements of a list and then called.


def func1():
    return (34, 87, 35)


def func2():
    return 'eqabq'


def func3():
    return 91


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 41.32


b = ["Hello"]
b[0] = func4

f = b[0]()
