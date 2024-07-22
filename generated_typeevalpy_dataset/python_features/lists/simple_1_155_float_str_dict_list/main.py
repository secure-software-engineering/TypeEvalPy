# Functions are assigned as elements of a list and then called.


def func1():
    return 96.97


def func2():
    return 'ygqfw'


def func3():
    return {'bglfn': 95, 'jvyny': 56, 'jwbii': 88}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [21, 66, 7]


b = ["Hello"]
b[0] = func4

f = b[0]()
