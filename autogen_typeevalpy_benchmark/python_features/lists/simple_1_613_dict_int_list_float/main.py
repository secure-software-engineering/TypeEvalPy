# Functions are assigned as elements of a list and then called.


def func1():
    return {'djhka': 59, 'vmaom': 15, 'yuvfa': 20}


def func2():
    return 15


def func3():
    return [52, 95, 56]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 18.81


b = ["Hello"]
b[0] = func4

f = b[0]()
