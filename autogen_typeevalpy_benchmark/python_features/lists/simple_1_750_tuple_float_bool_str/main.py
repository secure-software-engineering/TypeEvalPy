# Functions are assigned as elements of a list and then called.


def func1():
    return (41, 76, 77)


def func2():
    return 96.04


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'nlmvj'


b = ["Hello"]
b[0] = func4

f = b[0]()
