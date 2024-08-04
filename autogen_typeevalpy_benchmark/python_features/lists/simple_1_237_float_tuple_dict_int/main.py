# Functions are assigned as elements of a list and then called.


def func1():
    return 39.57


def func2():
    return (3, 42, 31)


def func3():
    return {'tpxzx': 94, 'caawm': 53, 'gwznz': 27}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 62


b = ["Hello"]
b[0] = func4

f = b[0]()
