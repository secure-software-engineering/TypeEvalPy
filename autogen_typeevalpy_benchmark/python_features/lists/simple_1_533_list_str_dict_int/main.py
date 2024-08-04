# Functions are assigned as elements of a list and then called.


def func1():
    return [48, 17, 22]


def func2():
    return 'szqcw'


def func3():
    return {'pynel': 85, 'zokar': 75, 'zggjb': 43}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 91


b = ["Hello"]
b[0] = func4

f = b[0]()
