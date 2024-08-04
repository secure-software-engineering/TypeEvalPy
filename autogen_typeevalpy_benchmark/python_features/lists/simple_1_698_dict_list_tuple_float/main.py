# Functions are assigned as elements of a list and then called.


def func1():
    return {'hbcqi': 17, 'oztdn': 12, 'dmjpo': 41}


def func2():
    return [61, 86, 65]


def func3():
    return (55, 33, 91)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 28.33


b = ["Hello"]
b[0] = func4

f = b[0]()
