# Functions are assigned as elements of a list and then called.


def func1():
    return [45, 1, 76]


def func2():
    return 'mwfxp'


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'bwnsv': 50, 'xotmh': 27, 'lrhxy': 85}


b = ["Hello"]
b[0] = func4

f = b[0]()
