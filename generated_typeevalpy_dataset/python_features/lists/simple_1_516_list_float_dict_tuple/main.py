# Functions are assigned as elements of a list and then called.


def func1():
    return [96, 75, 27]


def func2():
    return 22.45


def func3():
    return {'wqwal': 94, 'xpkzv': 15, 'bgzsu': 52}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (15, 95, 78)


b = ["Hello"]
b[0] = func4

f = b[0]()
