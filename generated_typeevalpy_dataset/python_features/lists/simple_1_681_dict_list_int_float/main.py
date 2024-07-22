# Functions are assigned as elements of a list and then called.


def func1():
    return {'zwioo': 46, 'mwgay': 93, 'uhwxv': 4}


def func2():
    return [82, 1, 71]


def func3():
    return 15


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 38.0


b = ["Hello"]
b[0] = func4

f = b[0]()
