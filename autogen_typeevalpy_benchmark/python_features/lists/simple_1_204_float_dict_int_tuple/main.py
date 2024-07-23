# Functions are assigned as elements of a list and then called.


def func1():
    return 17.83


def func2():
    return {'mkutq': 19, 'ngtqv': 2, 'lenwz': 34}


def func3():
    return 16


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (83, 77, 39)


b = ["Hello"]
b[0] = func4

f = b[0]()
