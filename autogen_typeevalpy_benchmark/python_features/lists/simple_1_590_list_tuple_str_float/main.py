# Functions are assigned as elements of a list and then called.


def func1():
    return [56, 82, 24]


def func2():
    return (90, 34, 48)


def func3():
    return 'dajoe'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 82.24


b = ["Hello"]
b[0] = func4

f = b[0]()
