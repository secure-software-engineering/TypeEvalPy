# Functions are assigned as elements of a list and then called.


def func1():
    return {'ohtpn': 93, 'enlmy': 84, 'rktre': 17}


def func2():
    return 90.4


def func3():
    return 'wubbc'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [64, 2, 21]


b = ["Hello"]
b[0] = func4

f = b[0]()
