# Functions are assigned as elements of a list and then called.


def func1():
    return 15.6


def func2():
    return {'eedok': 29, 'auinf': 40, 'zexfm': 34}


def func3():
    return [18, 35, 10]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 99


b = ["Hello"]
b[0] = func4

f = b[0]()
