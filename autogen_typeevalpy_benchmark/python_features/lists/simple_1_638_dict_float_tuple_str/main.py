# Functions are assigned as elements of a list and then called.


def func1():
    return {'hxfct': 3, 'szmhy': 98, 'sczjt': 19}


def func2():
    return 39.73


def func3():
    return (16, 87, 7)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'dtvzd'


b = ["Hello"]
b[0] = func4

f = b[0]()
