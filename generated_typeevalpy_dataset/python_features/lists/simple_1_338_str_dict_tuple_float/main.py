# Functions are assigned as elements of a list and then called.


def func1():
    return 'xcafu'


def func2():
    return {'rbvkt': 4, 'fozum': 6, 'khrma': 65}


def func3():
    return (28, 72, 32)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 14.14


b = ["Hello"]
b[0] = func4

f = b[0]()
