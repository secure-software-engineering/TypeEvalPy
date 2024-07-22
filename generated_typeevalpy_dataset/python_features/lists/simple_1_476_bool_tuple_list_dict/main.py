# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return (65, 22, 60)


def func3():
    return [67, 59, 22]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'dibbf': 52, 'qbvoa': 64, 'rsmec': 42}


b = ["Hello"]
b[0] = func4

f = b[0]()
