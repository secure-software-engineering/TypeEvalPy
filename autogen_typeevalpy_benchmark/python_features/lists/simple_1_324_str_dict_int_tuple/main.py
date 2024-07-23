# Functions are assigned as elements of a list and then called.


def func1():
    return 'dzskz'


def func2():
    return {'jwyhs': 70, 'uzuaw': 72, 'osvgd': 50}


def func3():
    return 21


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (14, 41, 35)


b = ["Hello"]
b[0] = func4

f = b[0]()
