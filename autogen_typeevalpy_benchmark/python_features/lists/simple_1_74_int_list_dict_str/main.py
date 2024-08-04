# Functions are assigned as elements of a list and then called.


def func1():
    return 68


def func2():
    return [37, 48, 66]


def func3():
    return {'fcaof': 82, 'jrnmj': 10, 'rsmae': 78}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ehcag'


b = ["Hello"]
b[0] = func4

f = b[0]()
