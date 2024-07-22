# Functions are assigned as elements of a list and then called.


def func1():
    return (94, 20, 82)


def func2():
    return 91.39


def func3():
    return {'jveuz': 62, 'cgzni': 20, 'xprrv': 18}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
