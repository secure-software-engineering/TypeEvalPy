# Functions are assigned as elements of a list and then called.


def func1():
    return {'veqkq': 100, 'nxatl': 10, 'htxwy': 14}


def func2():
    return (96, 92, 22)


def func3():
    return 7.41


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'pnufu'


b = ["Hello"]
b[0] = func4

f = b[0]()
