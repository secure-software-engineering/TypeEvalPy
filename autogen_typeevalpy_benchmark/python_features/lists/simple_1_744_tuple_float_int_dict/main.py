# Functions are assigned as elements of a list and then called.


def func1():
    return (68, 39, 31)


def func2():
    return 11.0


def func3():
    return 81


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ibjwa': 77, 'enysd': 44, 'kuncj': 50}


b = ["Hello"]
b[0] = func4

f = b[0]()
