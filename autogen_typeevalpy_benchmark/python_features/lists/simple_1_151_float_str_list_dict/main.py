# Functions are assigned as elements of a list and then called.


def func1():
    return 44.31


def func2():
    return 'rkhks'


def func3():
    return [61, 44, 21]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'saqvg': 78, 'balym': 80, 'bzphj': 86}


b = ["Hello"]
b[0] = func4

f = b[0]()
