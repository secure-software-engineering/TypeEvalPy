# Functions are assigned as elements of a list and then called.


def func1():
    return {'jyqvi': 70, 'fycld': 70, 'efddi': 14}


def func2():
    return 6.5


def func3():
    return (96, 30, 83)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 32


b = ["Hello"]
b[0] = func4

f = b[0]()
