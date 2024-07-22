# Functions are assigned as elements of a list and then called.


def func1():
    return (65, 93, 18)


def func2():
    return 68


def func3():
    return 'pyvcl'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'eorld': 94, 'otknx': 46, 'ovunt': 62}


b = ["Hello"]
b[0] = func4

f = b[0]()
