# Functions are assigned as elements of a list and then called.


def func1():
    return 'ugrfi'


def func2():
    return (61, 74, 7)


def func3():
    return {'wxtmc': 23, 'llknq': 82, 'uifgx': 74}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 7.04


b = ["Hello"]
b[0] = func4

f = b[0]()
