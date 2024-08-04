# Functions are assigned as elements of a list and then called.


def func1():
    return 97.09


def func2():
    return [11, 90, 34]


def func3():
    return 23


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'djdtc': 85, 'dsmfu': 51, 'cgnlu': 15}


b = ["Hello"]
b[0] = func4

f = b[0]()
