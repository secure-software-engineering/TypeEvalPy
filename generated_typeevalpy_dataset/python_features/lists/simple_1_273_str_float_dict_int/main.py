# Functions are assigned as elements of a list and then called.


def func1():
    return 'toums'


def func2():
    return 69.94


def func3():
    return {'oerbg': 26, 'julcd': 62, 'zrpul': 74}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 11


b = ["Hello"]
b[0] = func4

f = b[0]()
