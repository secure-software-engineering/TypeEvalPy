# Functions are assigned as elements of a list and then called.


def func1():
    return 'sonfu'


def func2():
    return 23.45


def func3():
    return 12


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ggewn': 34, 'yrnyq': 64, 'tyuli': 79}


b = ["Hello"]
b[0] = func4

f = b[0]()
