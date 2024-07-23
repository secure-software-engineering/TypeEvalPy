# Functions are assigned as elements of a list and then called.


def func1():
    return {'mgmrz': 58, 'oeeta': 98, 'sdohf': 21}


def func2():
    return 75


def func3():
    return (97, 14, 78)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [20, 75, 23]


b = ["Hello"]
b[0] = func4

f = b[0]()
