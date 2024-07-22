# Functions are assigned as elements of a list and then called.


def func1():
    return {'vecxn': 49, 'qtemm': 85, 'tnjyp': 80}


def func2():
    return (98, 70, 88)


def func3():
    return [48, 6, 42]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'oajpd'


b = ["Hello"]
b[0] = func4

f = b[0]()
