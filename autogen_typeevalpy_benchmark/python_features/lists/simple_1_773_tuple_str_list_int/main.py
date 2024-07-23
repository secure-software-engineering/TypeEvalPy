# Functions are assigned as elements of a list and then called.


def func1():
    return (4, 16, 5)


def func2():
    return 'tvopo'


def func3():
    return [68, 5, 27]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 33


b = ["Hello"]
b[0] = func4

f = b[0]()
