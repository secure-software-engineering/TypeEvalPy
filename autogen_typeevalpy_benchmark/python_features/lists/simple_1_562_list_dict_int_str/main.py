# Functions are assigned as elements of a list and then called.


def func1():
    return [68, 90, 50]


def func2():
    return {'hyvts': 63, 'mtutx': 5, 'dmfno': 56}


def func3():
    return 7


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ikaly'


b = ["Hello"]
b[0] = func4

f = b[0]()
