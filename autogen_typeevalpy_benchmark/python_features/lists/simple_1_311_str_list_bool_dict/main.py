# Functions are assigned as elements of a list and then called.


def func1():
    return 'ewpwe'


def func2():
    return [27, 12, 65]


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'cykgh': 97, 'uvpcg': 46, 'cnhul': 87}


b = ["Hello"]
b[0] = func4

f = b[0]()
