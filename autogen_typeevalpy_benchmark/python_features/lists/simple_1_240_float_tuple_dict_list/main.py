# Functions are assigned as elements of a list and then called.


def func1():
    return 47.77


def func2():
    return (78, 69, 22)


def func3():
    return {'ejvdz': 10, 'pxyxo': 23, 'nuope': 11}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [21, 52, 28]


b = ["Hello"]
b[0] = func4

f = b[0]()
