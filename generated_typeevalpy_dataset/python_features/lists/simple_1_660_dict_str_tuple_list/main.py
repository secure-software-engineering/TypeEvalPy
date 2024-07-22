# Functions are assigned as elements of a list and then called.


def func1():
    return {'xaiei': 30, 'rueqx': 37, 'udbjy': 46}


def func2():
    return 'piciy'


def func3():
    return (14, 72, 57)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [11, 12, 70]


b = ["Hello"]
b[0] = func4

f = b[0]()
