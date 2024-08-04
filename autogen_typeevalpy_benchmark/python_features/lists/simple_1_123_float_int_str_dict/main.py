# Functions are assigned as elements of a list and then called.


def func1():
    return 9.92


def func2():
    return 55


def func3():
    return 'onpen'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'dhovc': 83, 'fdmfl': 57, 'qqszr': 30}


b = ["Hello"]
b[0] = func4

f = b[0]()
