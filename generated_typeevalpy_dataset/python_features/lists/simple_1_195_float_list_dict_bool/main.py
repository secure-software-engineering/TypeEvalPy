# Functions are assigned as elements of a list and then called.


def func1():
    return 51.09


def func2():
    return [47, 2, 96]


def func3():
    return {'buynx': 31, 'blile': 45, 'crcot': 62}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
