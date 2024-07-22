# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return {'ixxxe': 30, 'fngbq': 92, 'gktde': 54}


def func3():
    return (22, 6, 14)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 34.13


b = ["Hello"]
b[0] = func4

f = b[0]()
