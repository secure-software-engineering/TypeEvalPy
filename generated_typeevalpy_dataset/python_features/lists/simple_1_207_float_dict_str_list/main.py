# Functions are assigned as elements of a list and then called.


def func1():
    return 21.1


def func2():
    return {'fvjpd': 57, 'naddc': 33, 'dtbem': 44}


def func3():
    return 'wrkev'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [69, 86, 19]


b = ["Hello"]
b[0] = func4

f = b[0]()
