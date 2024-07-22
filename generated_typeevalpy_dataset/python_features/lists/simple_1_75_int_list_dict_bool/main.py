# Functions are assigned as elements of a list and then called.


def func1():
    return 81


def func2():
    return [59, 49, 74]


def func3():
    return {'cxcqr': 77, 'xouci': 48, 'udjmr': 8}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
