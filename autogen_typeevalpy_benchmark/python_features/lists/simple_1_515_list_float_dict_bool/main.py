# Functions are assigned as elements of a list and then called.


def func1():
    return [44, 82, 38]


def func2():
    return 20.01


def func3():
    return {'zufpq': 25, 'ubebb': 94, 'drzfm': 71}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
