# Functions are assigned as elements of a list and then called.


def func1():
    return 61


def func2():
    return {'gxohu': 48, 'ryslo': 34, 'kibgv': 52}


def func3():
    return (1, 96, 96)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
