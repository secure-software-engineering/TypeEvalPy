# Functions are assigned as elements of a list and then called.


def func1():
    return 'civku'


def func2():
    return {'ablqo': 68, 'bndzy': 20, 'iewab': 12}


def func3():
    return 75


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
