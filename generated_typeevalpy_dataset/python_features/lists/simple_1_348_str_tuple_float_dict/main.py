# Functions are assigned as elements of a list and then called.


def func1():
    return 'qqnei'


def func2():
    return (20, 99, 95)


def func3():
    return 34.89


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ydexi': 80, 'hxowm': 33, 'ljdvk': 76}


b = ["Hello"]
b[0] = func4

f = b[0]()
