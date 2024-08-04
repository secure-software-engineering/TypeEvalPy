# Functions are assigned as elements of a list and then called.


def func1():
    return {'arbge': 95, 'ynlus': 96, 'yftml': 89}


def func2():
    return 93.28


def func3():
    return 'xqapi'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 18


b = ["Hello"]
b[0] = func4

f = b[0]()
