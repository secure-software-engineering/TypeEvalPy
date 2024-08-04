# Functions are assigned as elements of a list and then called.


def func1():
    return [60, 35, 54]


def func2():
    return (8, 2, 32)


def func3():
    return {'wctwy': 34, 'oulvj': 44, 'mphto': 2}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 84.65


b = ["Hello"]
b[0] = func4

f = b[0]()
