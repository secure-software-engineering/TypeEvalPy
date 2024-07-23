# Functions are assigned as elements of a list and then called.


def func1():
    return 83.36


def func2():
    return 'gxrpr'


def func3():
    return {'dipfo': 40, 'zlaxv': 47, 'phklo': 69}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [76, 81, 47]


b = ["Hello"]
b[0] = func4

f = b[0]()
