# Functions are assigned as elements of a list and then called.


def func1():
    return {'bqjop': 8, 'fbezq': 6, 'bqufd': 68}


def func2():
    return (18, 68, 68)


def func3():
    return 'efiwk'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 31.32


b = ["Hello"]
b[0] = func4

f = b[0]()
