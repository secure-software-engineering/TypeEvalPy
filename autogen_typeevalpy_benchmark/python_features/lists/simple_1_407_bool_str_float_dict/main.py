# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return 'hanmd'


def func3():
    return 96.85


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'vthfm': 52, 'igqdm': 58, 'actvt': 47}


b = ["Hello"]
b[0] = func4

f = b[0]()
