# Functions are assigned as elements of a list and then called.


def func1():
    return 41.65


def func2():
    return {'rkumg': 95, 'geoki': 95, 'tvfmo': 62}


def func3():
    return 'eavee'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (63, 18, 33)


b = ["Hello"]
b[0] = func4

f = b[0]()
