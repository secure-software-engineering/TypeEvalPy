# Functions are assigned as elements of a list and then called.


def func1():
    return 64.2


def func2():
    return (57, 37, 98)


def func3():
    return [97, 8, 79]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'jngqy': 62, 'upmlh': 97, 'zupot': 25}


b = ["Hello"]
b[0] = func4

f = b[0]()
