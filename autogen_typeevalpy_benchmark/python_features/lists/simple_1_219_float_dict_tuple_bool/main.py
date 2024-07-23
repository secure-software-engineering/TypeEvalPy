# Functions are assigned as elements of a list and then called.


def func1():
    return 82.32


def func2():
    return {'wsaig': 74, 'odqhv': 48, 'yydcf': 19}


def func3():
    return (90, 97, 63)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
