# Functions are assigned as elements of a list and then called.


def func1():
    return [2, 40, 70]


def func2():
    return (5, 13, 27)


def func3():
    return 59.03


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'tfego'


b = ["Hello"]
b[0] = func4

f = b[0]()
