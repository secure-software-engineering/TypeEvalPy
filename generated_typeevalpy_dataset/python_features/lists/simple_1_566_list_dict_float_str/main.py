# Functions are assigned as elements of a list and then called.


def func1():
    return [27, 68, 44]


def func2():
    return {'wbjaq': 33, 'ybyeh': 13, 'yzxyk': 46}


def func3():
    return 46.03


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'wqprv'


b = ["Hello"]
b[0] = func4

f = b[0]()
