# Functions are assigned as elements of a list and then called.


def func1():
    return (78, 82, 8)


def func2():
    return [47, 21, 75]


def func3():
    return {'vaxox': 17, 'vsmrk': 2, 'jrndb': 87}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 94.79


b = ["Hello"]
b[0] = func4

f = b[0]()
