# Functions are assigned as elements of a list and then called.


def func1():
    return 74.15


def func2():
    return {'rjcwv': 88, 'ylavb': 87, 'eqgsx': 4}


def func3():
    return 'jdoub'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
