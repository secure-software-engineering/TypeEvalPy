# Functions are assigned as elements of a list and then called.


def func1():
    return {'vativ': 77, 'ryupa': 93, 'zscfm': 59}


def func2():
    return 'mwsvm'


def func3():
    return 7


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [26, 28, 61]


b = ["Hello"]
b[0] = func4

f = b[0]()
