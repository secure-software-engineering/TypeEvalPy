# Functions are assigned as elements of a list and then called.


def func1():
    return 67.15


def func2():
    return True


def func3():
    return [99, 1, 1]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'poglc': 85, 'vtsve': 51, 'lkhew': 64}


b = ["Hello"]
b[0] = func4

f = b[0]()
