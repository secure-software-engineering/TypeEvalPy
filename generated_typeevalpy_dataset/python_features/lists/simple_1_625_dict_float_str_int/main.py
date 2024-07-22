# Functions are assigned as elements of a list and then called.


def func1():
    return {'iwikn': 30, 'bysfc': 16, 'cyncj': 89}


def func2():
    return 84.5


def func3():
    return 'ceyhl'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 63


b = ["Hello"]
b[0] = func4

f = b[0]()
