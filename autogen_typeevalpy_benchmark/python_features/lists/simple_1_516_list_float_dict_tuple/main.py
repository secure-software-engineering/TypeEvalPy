# Functions are assigned as elements of a list and then called.


def func1():
    return [64, 30, 64]


def func2():
    return 62.32


def func3():
    return {'myplh': 34, 'tcufo': 98, 'gcour': 2}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (62, 35, 33)


b = ["Hello"]
b[0] = func4

f = b[0]()
