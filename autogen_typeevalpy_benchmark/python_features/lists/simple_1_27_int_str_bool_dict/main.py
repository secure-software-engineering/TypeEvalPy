# Functions are assigned as elements of a list and then called.


def func1():
    return 76


def func2():
    return 'prmjd'


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'rasfp': 85, 'ofohb': 73, 'mvkov': 85}


b = ["Hello"]
b[0] = func4

f = b[0]()
