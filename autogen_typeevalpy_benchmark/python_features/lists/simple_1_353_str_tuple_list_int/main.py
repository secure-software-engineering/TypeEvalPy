# Functions are assigned as elements of a list and then called.


def func1():
    return 'dazbc'


def func2():
    return (88, 1, 29)


def func3():
    return [78, 12, 9]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 15


b = ["Hello"]
b[0] = func4

f = b[0]()
