# Functions are assigned as elements of a list and then called.


def func1():
    return {'ngvyl': 34, 'rzbqu': 75, 'ijden': 14}


def func2():
    return [37, 70, 1]


def func3():
    return 'ogocn'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 26


b = ["Hello"]
b[0] = func4

f = b[0]()
