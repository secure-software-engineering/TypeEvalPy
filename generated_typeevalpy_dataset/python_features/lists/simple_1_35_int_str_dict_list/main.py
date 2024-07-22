# Functions are assigned as elements of a list and then called.


def func1():
    return 51


def func2():
    return 'rzvxc'


def func3():
    return {'oiktt': 59, 'qcpyc': 77, 'gljzm': 80}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [61, 76, 35]


b = ["Hello"]
b[0] = func4

f = b[0]()
