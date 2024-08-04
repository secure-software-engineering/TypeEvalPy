# Functions are assigned as elements of a list and then called.


def func1():
    return (45, 26, 78)


def func2():
    return {'vohgb': 21, 'xwoky': 47, 'nwyvl': 33}


def func3():
    return [43, 100, 22]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 87.32


b = ["Hello"]
b[0] = func4

f = b[0]()
