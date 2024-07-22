# Functions are assigned as elements of a list and then called.


def func1():
    return {'wusfw': 94, 'xpvup': 65, 'rrcar': 4}


def func2():
    return False


def func3():
    return 12.39


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 30


b = ["Hello"]
b[0] = func4

f = b[0]()
