# Functions are assigned as elements of a list and then called.


def func1():
    return (5, 65, 15)


def func2():
    return [81, 19, 14]


def func3():
    return 'arpup'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 29.94


b = ["Hello"]
b[0] = func4

f = b[0]()
