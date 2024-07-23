# Functions are assigned as elements of a list and then called.


def func1():
    return 22


def func2():
    return [60, 36, 80]


def func3():
    return {'fbsmk': 93, 'lyfvx': 62, 'wnhqy': 11}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'gfkws'


b = ["Hello"]
b[0] = func4

f = b[0]()
