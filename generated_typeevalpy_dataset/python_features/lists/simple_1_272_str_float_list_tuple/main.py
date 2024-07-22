# Functions are assigned as elements of a list and then called.


def func1():
    return 'njqto'


def func2():
    return 95.92


def func3():
    return [40, 33, 72]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (60, 77, 58)


b = ["Hello"]
b[0] = func4

f = b[0]()
