# Functions are assigned as elements of a list and then called.


def func1():
    return 31


def func2():
    return {'gbidm': 16, 'jokvc': 68, 'sbajc': 49}


def func3():
    return 17.11


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (94, 35, 64)


b = ["Hello"]
b[0] = func4

f = b[0]()
