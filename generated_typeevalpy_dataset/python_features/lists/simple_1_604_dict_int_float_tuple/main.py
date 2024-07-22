# Functions are assigned as elements of a list and then called.


def func1():
    return {'qrrvy': 44, 'gtidw': 34, 'muuna': 84}


def func2():
    return 19


def func3():
    return 93.09


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (70, 63, 53)


b = ["Hello"]
b[0] = func4

f = b[0]()
