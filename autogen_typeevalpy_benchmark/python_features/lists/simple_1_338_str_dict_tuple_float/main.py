# Functions are assigned as elements of a list and then called.


def func1():
    return 'xbmma'


def func2():
    return {'gfofu': 68, 'wlmrt': 26, 'vjxxy': 22}


def func3():
    return (65, 51, 5)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 27.12


b = ["Hello"]
b[0] = func4

f = b[0]()
