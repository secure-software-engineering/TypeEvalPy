# Functions are assigned as elements of a list and then called.


def func1():
    return 21


def func2():
    return (72, 86, 64)


def func3():
    return 'bxgwj'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [51, 55, 58]


b = ["Hello"]
b[0] = func4

f = b[0]()
