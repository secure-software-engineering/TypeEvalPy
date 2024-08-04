# Functions are assigned as elements of a list and then called.


def func1():
    return (29, 11, 11)


def func2():
    return {'jzmxr': 11, 'qwawt': 91, 'rtryz': 23}


def func3():
    return 2.71


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'rifiu'


b = ["Hello"]
b[0] = func4

f = b[0]()
