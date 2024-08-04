# Functions are assigned as elements of a list and then called.


def func1():
    return [27, 96, 88]


def func2():
    return 36.99


def func3():
    return 'yiigi'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'qqiic': 52, 'hkbgm': 94, 'xgzno': 5}


b = ["Hello"]
b[0] = func4

f = b[0]()
