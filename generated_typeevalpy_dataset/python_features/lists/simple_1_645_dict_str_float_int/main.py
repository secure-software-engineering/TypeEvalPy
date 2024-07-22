# Functions are assigned as elements of a list and then called.


def func1():
    return {'ucsxn': 33, 'wpxfj': 20, 'lyvxd': 39}


def func2():
    return 'ztzqd'


def func3():
    return 35.38


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 28


b = ["Hello"]
b[0] = func4

f = b[0]()
