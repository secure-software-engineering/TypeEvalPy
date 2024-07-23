# Functions are assigned as elements of a list and then called.


def func1():
    return 98


def func2():
    return 47.85


def func3():
    return [80, 12, 99]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'kzpmx': 14, 'owgeb': 38, 'dszaq': 84}


b = ["Hello"]
b[0] = func4

f = b[0]()
