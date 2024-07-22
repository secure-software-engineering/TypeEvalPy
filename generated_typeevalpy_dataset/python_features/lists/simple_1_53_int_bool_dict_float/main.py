# Functions are assigned as elements of a list and then called.


def func1():
    return 71


def func2():
    return True


def func3():
    return {'jhuog': 13, 'bwtqd': 7, 'jwmvr': 83}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 26.16


b = ["Hello"]
b[0] = func4

f = b[0]()
