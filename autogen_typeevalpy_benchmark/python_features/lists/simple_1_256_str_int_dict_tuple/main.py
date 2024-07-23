# Functions are assigned as elements of a list and then called.


def func1():
    return 'pmlny'


def func2():
    return 2


def func3():
    return {'vlcax': 98, 'durcb': 98, 'gofbi': 6}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (48, 56, 17)


b = ["Hello"]
b[0] = func4

f = b[0]()
