# Functions are assigned as elements of a list and then called.


def func1():
    return 'eofbz'


def func2():
    return 90.3


def func3():
    return [29, 25, 29]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (42, 82, 96)


b = ["Hello"]
b[0] = func4

f = b[0]()
