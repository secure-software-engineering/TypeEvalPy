# Functions are assigned as elements of a list and then called.


def func1():
    return (13, 75, 93)


def func2():
    return {'oqekd': 87, 'jgxve': 83, 'vemfi': 62}


def func3():
    return 57


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [47, 64, 3]


b = ["Hello"]
b[0] = func4

f = b[0]()
