# Functions are assigned as elements of a list and then called.


def func1():
    return 88.21


def func2():
    return {'wnoyr': 65, 'goqhy': 94, 'erfyd': 39}


def func3():
    return [55, 97, 51]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'dplbs'


b = ["Hello"]
b[0] = func4

f = b[0]()
