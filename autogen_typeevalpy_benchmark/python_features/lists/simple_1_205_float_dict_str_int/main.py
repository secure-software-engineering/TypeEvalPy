# Functions are assigned as elements of a list and then called.


def func1():
    return 19.41


def func2():
    return {'yndwz': 44, 'mvhlg': 54, 'lxttl': 27}


def func3():
    return 'rchkq'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 91


b = ["Hello"]
b[0] = func4

f = b[0]()
