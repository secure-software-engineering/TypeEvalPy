# Functions are assigned as elements of a list and then called.


def func1():
    return 31.35


def func2():
    return {'giegg': 69, 'brolx': 53, 'ujbcj': 41}


def func3():
    return 'tzzge'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
