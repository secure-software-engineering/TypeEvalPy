# Functions are assigned as elements of a list and then called.


def func1():
    return 'zrcyy'


def func2():
    return [34, 5, 55]


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (83, 35, 64)


b = ["Hello"]
b[0] = func4

f = b[0]()
