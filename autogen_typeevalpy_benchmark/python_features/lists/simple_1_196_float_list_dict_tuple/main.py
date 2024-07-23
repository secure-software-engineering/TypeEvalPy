# Functions are assigned as elements of a list and then called.


def func1():
    return 46.56


def func2():
    return [36, 89, 90]


def func3():
    return {'whxvl': 85, 'wvpuo': 68, 'nxwtl': 21}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (18, 42, 67)


b = ["Hello"]
b[0] = func4

f = b[0]()
