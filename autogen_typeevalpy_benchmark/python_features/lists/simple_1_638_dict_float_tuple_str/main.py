# Functions are assigned as elements of a list and then called.


def func1():
    return {'eljam': 84, 'gfkjd': 85, 'huwyv': 87}


def func2():
    return 30.38


def func3():
    return (35, 7, 45)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'dcxlr'


b = ["Hello"]
b[0] = func4

f = b[0]()
