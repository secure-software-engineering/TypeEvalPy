# Functions are assigned as elements of a list and then called.


def func1():
    return {'jxnte': 1, 'feobv': 81, 'eothk': 84}


def func2():
    return 81


def func3():
    return [92, 85, 52]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'zninp'


b = ["Hello"]
b[0] = func4

f = b[0]()
