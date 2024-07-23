# Functions are assigned as elements of a list and then called.


def func1():
    return 83


def func2():
    return 'bzzvz'


def func3():
    return {'xzjrv': 3, 'maikc': 96, 'yaffg': 63}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (9, 17, 100)


b = ["Hello"]
b[0] = func4

f = b[0]()
