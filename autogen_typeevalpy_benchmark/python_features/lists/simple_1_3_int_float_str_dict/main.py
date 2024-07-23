# Functions are assigned as elements of a list and then called.


def func1():
    return 8


def func2():
    return 58.1


def func3():
    return 'bswkt'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'wdjrv': 46, 'trrxh': 91, 'bvuan': 72}


b = ["Hello"]
b[0] = func4

f = b[0]()
