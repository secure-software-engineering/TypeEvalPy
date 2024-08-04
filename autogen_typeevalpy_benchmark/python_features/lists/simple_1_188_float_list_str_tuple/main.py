# Functions are assigned as elements of a list and then called.


def func1():
    return 44.8


def func2():
    return [80, 65, 39]


def func3():
    return 'nyijk'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (16, 45, 13)


b = ["Hello"]
b[0] = func4

f = b[0]()
