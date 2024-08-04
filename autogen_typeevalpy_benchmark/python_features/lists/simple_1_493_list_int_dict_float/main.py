# Functions are assigned as elements of a list and then called.


def func1():
    return [23, 69, 74]


def func2():
    return 9


def func3():
    return {'gvial': 32, 'pjqcl': 28, 'worsj': 5}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 59.48


b = ["Hello"]
b[0] = func4

f = b[0]()
