# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return {'dddhn': 1, 'piltk': 65, 'ynszr': 34}


def func3():
    return 'xafzu'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [6, 31, 23]


b = ["Hello"]
b[0] = func4

f = b[0]()
