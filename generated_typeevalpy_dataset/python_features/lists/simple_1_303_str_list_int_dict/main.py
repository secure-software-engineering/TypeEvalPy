# Functions are assigned as elements of a list and then called.


def func1():
    return 'qrmfp'


def func2():
    return [11, 24, 43]


def func3():
    return 42


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'rmude': 52, 'nwqbk': 45, 'cyjzk': 46}


b = ["Hello"]
b[0] = func4

f = b[0]()
