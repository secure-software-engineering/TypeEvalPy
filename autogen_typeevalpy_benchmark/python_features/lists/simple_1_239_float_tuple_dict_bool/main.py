# Functions are assigned as elements of a list and then called.


def func1():
    return 88.88


def func2():
    return (44, 72, 34)


def func3():
    return {'pqqit': 85, 'aooib': 26, 'qblum': 42}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
