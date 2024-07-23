# Functions are assigned as elements of a list and then called.


def func1():
    return {'prodo': 4, 'gcmab': 40, 'stfav': 27}


def func2():
    return 'dpihn'


def func3():
    return 66.96


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (85, 69, 31)


b = ["Hello"]
b[0] = func4

f = b[0]()
