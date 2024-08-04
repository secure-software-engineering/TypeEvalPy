# Functions are assigned as elements of a list and then called.


def func1():
    return [22, 23, 42]


def func2():
    return 'souja'


def func3():
    return {'ckrbv': 29, 'ctfem': 57, 'wenhh': 46}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 44.38


b = ["Hello"]
b[0] = func4

f = b[0]()
