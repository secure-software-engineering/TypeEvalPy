# Functions are assigned as elements of a list and then called.


def func1():
    return {'yygnz': 63, 'fmfmg': 94, 'iviya': 7}


def func2():
    return 'lcaqc'


def func3():
    return 2


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [6, 3, 52]


b = ["Hello"]
b[0] = func4

f = b[0]()
