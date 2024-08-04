# Functions are assigned as elements of a list and then called.


def func1():
    return {'ahjtw': 1, 'vhwvv': 4, 'txpgh': 17}


def func2():
    return 'nodhz'


def func3():
    return 66.52


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [13, 38, 23]


b = ["Hello"]
b[0] = func4

f = b[0]()
