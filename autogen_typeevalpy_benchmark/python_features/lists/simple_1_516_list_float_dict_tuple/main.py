# Functions are assigned as elements of a list and then called.


def func1():
    return [5, 58, 95]


def func2():
    return 50.45


def func3():
    return {'ypvco': 26, 'kulay': 12, 'wynny': 56}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (42, 5, 77)


b = ["Hello"]
b[0] = func4

f = b[0]()
