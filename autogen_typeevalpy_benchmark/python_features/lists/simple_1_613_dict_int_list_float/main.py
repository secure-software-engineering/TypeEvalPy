# Functions are assigned as elements of a list and then called.


def func1():
    return {'mrxcv': 88, 'hqpcg': 45, 'onwbi': 21}


def func2():
    return 77


def func3():
    return [7, 31, 46]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 8.82


b = ["Hello"]
b[0] = func4

f = b[0]()
