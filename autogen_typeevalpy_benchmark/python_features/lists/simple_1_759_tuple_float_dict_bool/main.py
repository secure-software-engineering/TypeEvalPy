# Functions are assigned as elements of a list and then called.


def func1():
    return (53, 53, 67)


def func2():
    return 75.38


def func3():
    return {'pvhdo': 47, 'lmhey': 35, 'icyxy': 73}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
