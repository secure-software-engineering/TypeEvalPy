# Functions are assigned as elements of a list and then called.


def func1():
    return 'dsxvp'


def func2():
    return [39, 63, 52]


def func3():
    return {'aolzv': 75, 'rleoo': 50, 'fuhcj': 75}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 73.47


b = ["Hello"]
b[0] = func4

f = b[0]()
