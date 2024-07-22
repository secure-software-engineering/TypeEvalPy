# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return [48, 50, 32]


def func3():
    return (39, 94, 29)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'hfaxi': 36, 'fnefb': 42, 'vdajn': 53}


b = ["Hello"]
b[0] = func4

f = b[0]()
