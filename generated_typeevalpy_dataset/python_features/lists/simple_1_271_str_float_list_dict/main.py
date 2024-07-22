# Functions are assigned as elements of a list and then called.


def func1():
    return 'crrgi'


def func2():
    return 61.97


def func3():
    return [6, 77, 2]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'laklk': 45, 'exiix': 50, 'xzbmc': 100}


b = ["Hello"]
b[0] = func4

f = b[0]()
