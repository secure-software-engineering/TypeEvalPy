# Functions are assigned as elements of a list and then called.


def func1():
    return 51.99


def func2():
    return 29


def func3():
    return (33, 5, 22)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'mjarb': 77, 'vdacw': 34, 'rodov': 96}


b = ["Hello"]
b[0] = func4

f = b[0]()
