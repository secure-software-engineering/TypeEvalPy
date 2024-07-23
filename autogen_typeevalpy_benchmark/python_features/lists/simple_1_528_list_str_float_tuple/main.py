# Functions are assigned as elements of a list and then called.


def func1():
    return [56, 48, 34]


def func2():
    return 'iknuj'


def func3():
    return 90.58


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (25, 6, 32)


b = ["Hello"]
b[0] = func4

f = b[0]()
