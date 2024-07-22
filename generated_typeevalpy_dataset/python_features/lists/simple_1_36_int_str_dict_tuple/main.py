# Functions are assigned as elements of a list and then called.


def func1():
    return 95


def func2():
    return 'bxzvo'


def func3():
    return {'ccnvx': 30, 'tzalh': 2, 'gejxk': 38}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (74, 47, 25)


b = ["Hello"]
b[0] = func4

f = b[0]()
