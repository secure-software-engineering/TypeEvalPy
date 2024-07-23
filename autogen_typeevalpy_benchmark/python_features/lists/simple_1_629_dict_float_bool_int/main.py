# Functions are assigned as elements of a list and then called.


def func1():
    return {'ewjrf': 12, 'lspxq': 25, 'nzbwr': 64}


def func2():
    return 29.38


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 86


b = ["Hello"]
b[0] = func4

f = b[0]()
