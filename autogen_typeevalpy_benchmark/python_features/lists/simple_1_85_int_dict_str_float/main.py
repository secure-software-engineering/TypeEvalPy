# Functions are assigned as elements of a list and then called.


def func1():
    return 53


def func2():
    return {'bhneq': 37, 'kapkk': 8, 'pyatf': 67}


def func3():
    return 'yniiv'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 42.65


b = ["Hello"]
b[0] = func4

f = b[0]()
