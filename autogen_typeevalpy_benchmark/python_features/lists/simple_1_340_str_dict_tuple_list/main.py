# Functions are assigned as elements of a list and then called.


def func1():
    return 'ocdrz'


def func2():
    return {'gawdd': 31, 'ynatu': 57, 'hbowg': 26}


def func3():
    return (31, 28, 9)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [23, 79, 27]


b = ["Hello"]
b[0] = func4

f = b[0]()
