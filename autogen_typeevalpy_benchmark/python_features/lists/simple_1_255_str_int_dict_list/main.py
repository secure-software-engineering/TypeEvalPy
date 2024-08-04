# Functions are assigned as elements of a list and then called.


def func1():
    return 'kaayw'


def func2():
    return 30


def func3():
    return {'ismpc': 33, 'eybzo': 58, 'vifqt': 88}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [76, 51, 14]


b = ["Hello"]
b[0] = func4

f = b[0]()
