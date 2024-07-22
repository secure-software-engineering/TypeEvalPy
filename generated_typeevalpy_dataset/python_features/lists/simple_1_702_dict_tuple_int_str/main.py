# Functions are assigned as elements of a list and then called.


def func1():
    return {'lknyi': 40, 'xdmln': 36, 'cakrr': 41}


def func2():
    return (3, 87, 52)


def func3():
    return 78


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'wvsoh'


b = ["Hello"]
b[0] = func4

f = b[0]()
