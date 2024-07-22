# Functions are assigned as elements of a list and then called.


def func1():
    return 96.71


def func2():
    return [36, 41, 28]


def func3():
    return (2, 18, 59)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'vuhel': 48, 'ticjj': 19, 'ymhra': 95}


b = ["Hello"]
b[0] = func4

f = b[0]()
