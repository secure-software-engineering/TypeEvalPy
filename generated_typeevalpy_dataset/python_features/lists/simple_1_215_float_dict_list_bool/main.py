# Functions are assigned as elements of a list and then called.


def func1():
    return 97.29


def func2():
    return {'gmlfk': 2, 'vsxdw': 67, 'qypmz': 52}


def func3():
    return [28, 62, 39]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
