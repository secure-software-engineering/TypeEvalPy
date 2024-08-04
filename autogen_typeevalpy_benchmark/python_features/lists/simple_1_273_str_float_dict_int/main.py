# Functions are assigned as elements of a list and then called.


def func1():
    return 'yukxj'


def func2():
    return 36.22


def func3():
    return {'radrr': 1, 'ocypp': 11, 'dexog': 100}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 74


b = ["Hello"]
b[0] = func4

f = b[0]()
