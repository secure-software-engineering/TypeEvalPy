# Functions are assigned as elements of a list and then called.


def func1():
    return (13, 63, 47)


def func2():
    return {'yvvrp': 7, 'pqsgv': 4, 'qqxsw': 14}


def func3():
    return 18.75


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 81


b = ["Hello"]
b[0] = func4

f = b[0]()
