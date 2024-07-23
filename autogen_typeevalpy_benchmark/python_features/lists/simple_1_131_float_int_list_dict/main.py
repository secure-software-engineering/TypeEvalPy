# Functions are assigned as elements of a list and then called.


def func1():
    return 13.53


def func2():
    return 41


def func3():
    return [83, 55, 79]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'mbqvl': 35, 'rhnmg': 90, 'nyclm': 5}


b = ["Hello"]
b[0] = func4

f = b[0]()
