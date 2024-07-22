# Functions are assigned as elements of a list and then called.


def func1():
    return [2, 33, 96]


def func2():
    return {'odbgz': 23, 'gbycj': 29, 'nhraq': 85}


def func3():
    return (60, 22, 44)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 65


b = ["Hello"]
b[0] = func4

f = b[0]()
