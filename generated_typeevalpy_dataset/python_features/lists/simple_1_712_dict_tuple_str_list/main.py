# Functions are assigned as elements of a list and then called.


def func1():
    return {'hkfhk': 39, 'tsxvx': 52, 'aslkv': 76}


def func2():
    return (10, 13, 25)


def func3():
    return 'niqjc'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [34, 82, 16]


b = ["Hello"]
b[0] = func4

f = b[0]()