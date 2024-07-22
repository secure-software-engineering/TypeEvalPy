# Functions are assigned as elements of a list and then called.


def func1():
    return (68, 3, 37)


def func2():
    return 48.5


def func3():
    return 'ehfad'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'bzqah': 20, 'wohwc': 43, 'vmesw': 30}


b = ["Hello"]
b[0] = func4

f = b[0]()
