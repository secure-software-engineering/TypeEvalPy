# Functions are assigned as elements of a list and then called.


def func1():
    return (72, 92, 8)


def func2():
    return [67, 49, 85]


def func3():
    return 52


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'eajyn': 95, 'lxdab': 47, 'fzksb': 65}


b = ["Hello"]
b[0] = func4

f = b[0]()
