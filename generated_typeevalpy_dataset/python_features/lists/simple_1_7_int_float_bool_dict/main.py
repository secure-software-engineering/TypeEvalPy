# Functions are assigned as elements of a list and then called.


def func1():
    return 58


def func2():
    return 15.01


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'lmzse': 44, 'syxgb': 61, 'ozsxp': 88}


b = ["Hello"]
b[0] = func4

f = b[0]()
