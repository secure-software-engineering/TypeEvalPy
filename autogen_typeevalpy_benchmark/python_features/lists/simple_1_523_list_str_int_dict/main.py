# Functions are assigned as elements of a list and then called.


def func1():
    return [39, 21, 50]


def func2():
    return 'udhkm'


def func3():
    return 91


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'agtca': 68, 'bqewx': 76, 'qfipg': 46}


b = ["Hello"]
b[0] = func4

f = b[0]()
