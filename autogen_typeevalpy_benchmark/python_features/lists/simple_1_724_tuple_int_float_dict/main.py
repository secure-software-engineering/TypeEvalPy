# Functions are assigned as elements of a list and then called.


def func1():
    return (76, 13, 37)


def func2():
    return 78


def func3():
    return 95.49


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'mxcch': 72, 'cdjnu': 30, 'dmtbo': 38}


b = ["Hello"]
b[0] = func4

f = b[0]()
