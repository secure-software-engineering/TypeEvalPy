# Functions are assigned as elements of a list and then called.


def func1():
    return 69


def func2():
    return 12.26


def func3():
    return [18, 89, 32]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ifcmj': 59, 'blkpm': 12, 'xohmu': 70}


b = ["Hello"]
b[0] = func4

f = b[0]()
