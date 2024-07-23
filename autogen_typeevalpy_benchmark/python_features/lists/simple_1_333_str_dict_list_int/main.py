# Functions are assigned as elements of a list and then called.


def func1():
    return 'nxout'


def func2():
    return {'jvplj': 70, 'sfoix': 9, 'usegk': 50}


def func3():
    return [100, 20, 91]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 44


b = ["Hello"]
b[0] = func4

f = b[0]()
