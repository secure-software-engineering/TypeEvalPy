# Functions are assigned as elements of a list and then called.


def func1():
    return (58, 45, 29)


def func2():
    return {'bxyzw': 48, 'yplwe': 45, 'iyhpb': 17}


def func3():
    return [80, 13, 87]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 52


b = ["Hello"]
b[0] = func4

f = b[0]()
