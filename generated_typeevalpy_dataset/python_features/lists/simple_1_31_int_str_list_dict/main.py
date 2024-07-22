# Functions are assigned as elements of a list and then called.


def func1():
    return 71


def func2():
    return 'rzrnr'


def func3():
    return [84, 12, 23]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'smcwt': 21, 'gtyne': 17, 'qhika': 3}


b = ["Hello"]
b[0] = func4

f = b[0]()
