# Functions are assigned as elements of a list and then called.


def func1():
    return 'tqxvl'


def func2():
    return (7, 27, 22)


def func3():
    return {'ffedb': 47, 'pgwms': 72, 'ajiie': 7}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 22


b = ["Hello"]
b[0] = func4

f = b[0]()
