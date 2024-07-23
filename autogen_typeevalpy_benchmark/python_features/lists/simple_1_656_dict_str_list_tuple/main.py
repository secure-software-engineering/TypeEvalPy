# Functions are assigned as elements of a list and then called.


def func1():
    return {'qjnrj': 56, 'sdfyb': 22, 'lxmgm': 62}


def func2():
    return 'gfvpw'


def func3():
    return [8, 44, 16]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (4, 24, 86)


b = ["Hello"]
b[0] = func4

f = b[0]()
