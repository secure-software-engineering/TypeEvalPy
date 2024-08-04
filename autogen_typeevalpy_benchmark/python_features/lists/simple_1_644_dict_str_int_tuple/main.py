# Functions are assigned as elements of a list and then called.


def func1():
    return {'igzhv': 1, 'hbayr': 9, 'opnik': 87}


def func2():
    return 'osxzr'


def func3():
    return 74


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (27, 75, 73)


b = ["Hello"]
b[0] = func4

f = b[0]()
