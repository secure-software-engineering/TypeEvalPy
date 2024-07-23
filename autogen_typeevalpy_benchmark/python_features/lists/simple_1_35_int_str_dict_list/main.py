# Functions are assigned as elements of a list and then called.


def func1():
    return 95


def func2():
    return 'zfbqx'


def func3():
    return {'jzvex': 98, 'nlixk': 6, 'bnglp': 24}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [49, 10, 71]


b = ["Hello"]
b[0] = func4

f = b[0]()
