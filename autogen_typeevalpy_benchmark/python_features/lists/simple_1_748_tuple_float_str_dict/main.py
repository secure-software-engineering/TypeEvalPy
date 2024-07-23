# Functions are assigned as elements of a list and then called.


def func1():
    return (65, 80, 80)


def func2():
    return 64.99


def func3():
    return 'ynrlg'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ltthy': 90, 'agebp': 11, 'cchmc': 27}


b = ["Hello"]
b[0] = func4

f = b[0]()
