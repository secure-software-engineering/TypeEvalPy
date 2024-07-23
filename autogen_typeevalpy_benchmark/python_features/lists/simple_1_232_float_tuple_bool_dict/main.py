# Functions are assigned as elements of a list and then called.


def func1():
    return 78.72


def func2():
    return (82, 69, 13)


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'bchoj': 37, 'nwfxr': 88, 'mzjey': 9}


b = ["Hello"]
b[0] = func4

f = b[0]()
