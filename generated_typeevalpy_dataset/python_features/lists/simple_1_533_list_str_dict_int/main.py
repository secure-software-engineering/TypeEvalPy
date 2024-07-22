# Functions are assigned as elements of a list and then called.


def func1():
    return [37, 55, 48]


def func2():
    return 'blubp'


def func3():
    return {'ujlos': 46, 'diuhl': 54, 'bvrqi': 22}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 94


b = ["Hello"]
b[0] = func4

f = b[0]()
