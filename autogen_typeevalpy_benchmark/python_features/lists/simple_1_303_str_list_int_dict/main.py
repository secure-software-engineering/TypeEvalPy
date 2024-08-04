# Functions are assigned as elements of a list and then called.


def func1():
    return 'kshvm'


def func2():
    return [3, 88, 86]


def func3():
    return 67


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'giwzz': 80, 'efzir': 66, 'olzzk': 84}


b = ["Hello"]
b[0] = func4

f = b[0]()
