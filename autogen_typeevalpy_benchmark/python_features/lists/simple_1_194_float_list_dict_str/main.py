# Functions are assigned as elements of a list and then called.


def func1():
    return 92.32


def func2():
    return [20, 92, 6]


def func3():
    return {'eyibm': 49, 'kulvx': 91, 'rwfoo': 53}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'lbyrp'


b = ["Hello"]
b[0] = func4

f = b[0]()
