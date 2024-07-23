# Functions are assigned as elements of a list and then called.


def func1():
    return 93.97


def func2():
    return {'bcvne': 26, 'gnmlp': 8, 'oxevq': 31}


def func3():
    return 74


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
