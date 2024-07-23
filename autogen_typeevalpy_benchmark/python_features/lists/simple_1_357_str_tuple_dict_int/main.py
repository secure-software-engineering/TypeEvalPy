# Functions are assigned as elements of a list and then called.


def func1():
    return 'ffxfj'


def func2():
    return (47, 11, 37)


def func3():
    return {'lcmrr': 76, 'xerdv': 27, 'xgeqv': 48}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 36


b = ["Hello"]
b[0] = func4

f = b[0]()
