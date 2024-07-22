# Functions are assigned as elements of a list and then called.


def func1():
    return {'ezpvr': 59, 'dvsag': 43, 'ejhcv': 17}


def func2():
    return 'mliek'


def func3():
    return 71.57


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [52, 44, 45]


b = ["Hello"]
b[0] = func4

f = b[0]()
