# Functions are assigned as elements of a list and then called.


def func1():
    return [24, 65, 21]


def func2():
    return 56.63


def func3():
    return {'gfhrq': 11, 'ufdiq': 85, 'phatu': 89}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 91


b = ["Hello"]
b[0] = func4

f = b[0]()
