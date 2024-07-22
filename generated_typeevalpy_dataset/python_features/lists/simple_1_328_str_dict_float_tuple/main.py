# Functions are assigned as elements of a list and then called.


def func1():
    return 'inhdd'


def func2():
    return {'elrbo': 82, 'ydkvz': 38, 'iumjk': 88}


def func3():
    return 67.79


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (79, 31, 79)


b = ["Hello"]
b[0] = func4

f = b[0]()
