# Functions are assigned as elements of a list and then called.


def func1():
    return 'uipof'


def func2():
    return (13, 48, 47)


def func3():
    return 22.93


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 98


b = ["Hello"]
b[0] = func4

f = b[0]()
