# Functions are assigned as elements of a list and then called.


def func1():
    return 'pdest'


def func2():
    return 18


def func3():
    return (13, 39, 26)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [74, 17, 60]


b = ["Hello"]
b[0] = func4

f = b[0]()
