# Functions are assigned as elements of a list and then called.


def func1():
    return [8, 91, 77]


def func2():
    return (29, 72, 45)


def func3():
    return 65.76


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'qavid': 55, 'jvzuq': 43, 'dkefj': 96}


b = ["Hello"]
b[0] = func4

f = b[0]()
