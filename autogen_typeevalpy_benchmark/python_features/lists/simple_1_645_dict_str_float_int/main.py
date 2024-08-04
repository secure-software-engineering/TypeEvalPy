# Functions are assigned as elements of a list and then called.


def func1():
    return {'tmnyk': 77, 'swsxp': 81, 'psoty': 24}


def func2():
    return 'vmxoz'


def func3():
    return 94.71


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 90


b = ["Hello"]
b[0] = func4

f = b[0]()
