# Functions are assigned as elements of a list and then called.


def func1():
    return {'scxld': 51, 'byaau': 32, 'nrkgt': 21}


def func2():
    return 59


def func3():
    return 'unbbp'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (81, 55, 35)


b = ["Hello"]
b[0] = func4

f = b[0]()
