# Functions are assigned as elements of a list and then called.


def func1():
    return [74, 21, 36]


def func2():
    return 47


def func3():
    return {'pywtn': 8, 'htoui': 36, 'ijzbf': 72}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'cyoox'


b = ["Hello"]
b[0] = func4

f = b[0]()
