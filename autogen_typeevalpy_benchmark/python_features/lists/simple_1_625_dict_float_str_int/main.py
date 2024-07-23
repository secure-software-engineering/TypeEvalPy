# Functions are assigned as elements of a list and then called.


def func1():
    return {'lreia': 90, 'jpgzn': 14, 'fziqa': 93}


def func2():
    return 78.25


def func3():
    return 'qpukc'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 2


b = ["Hello"]
b[0] = func4

f = b[0]()
