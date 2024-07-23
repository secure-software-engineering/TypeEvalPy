# Functions are assigned as elements of a list and then called.


def func1():
    return {'xtjvk': 11, 'lvbua': 25, 'ngnci': 5}


def func2():
    return (2, 27, 64)


def func3():
    return 85.56


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'xmzaz'


b = ["Hello"]
b[0] = func4

f = b[0]()
