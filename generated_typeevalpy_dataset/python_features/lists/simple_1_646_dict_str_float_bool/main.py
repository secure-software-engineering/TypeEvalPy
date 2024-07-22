# Functions are assigned as elements of a list and then called.


def func1():
    return {'xpnot': 86, 'uyfsk': 8, 'vixhu': 54}


def func2():
    return 'zvcwd'


def func3():
    return 48.7


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
