# Functions are assigned as elements of a list and then called.


def func1():
    return 82.95


def func2():
    return {'htjpy': 65, 'wbexa': 6, 'fnzkw': 18}


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'hydnk'


b = ["Hello"]
b[0] = func4

f = b[0]()
