# Functions are assigned as elements of a list and then called.


def func1():
    return [5, 5, 76]


def func2():
    return True


def func3():
    return {'ziutd': 59, 'apfrn': 14, 'dogha': 39}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'vuqwy'


b = ["Hello"]
b[0] = func4

f = b[0]()
