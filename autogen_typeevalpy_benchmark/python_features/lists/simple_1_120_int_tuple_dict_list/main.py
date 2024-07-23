# Functions are assigned as elements of a list and then called.


def func1():
    return 48


def func2():
    return (44, 92, 27)


def func3():
    return {'mlpag': 30, 'fysxs': 54, 'grawv': 2}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [34, 8, 27]


b = ["Hello"]
b[0] = func4

f = b[0]()
