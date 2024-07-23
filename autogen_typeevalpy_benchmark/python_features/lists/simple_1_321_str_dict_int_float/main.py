# Functions are assigned as elements of a list and then called.


def func1():
    return 'bpdll'


def func2():
    return {'oqtgx': 13, 'xgnwc': 18, 'yefmp': 19}


def func3():
    return 55


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 57.49


b = ["Hello"]
b[0] = func4

f = b[0]()
