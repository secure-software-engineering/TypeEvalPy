# Functions are assigned as elements of a list and then called.


def func1():
    return 81.69


def func2():
    return 'gsfup'


def func3():
    return 20


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [42, 77, 93]


b = ["Hello"]
b[0] = func4

f = b[0]()
