# Functions are assigned as elements of a list and then called.


def func1():
    return [51, 44, 33]


def func2():
    return (64, 100, 52)


def func3():
    return {'qrpgb': 28, 'yndfj': 71, 'pcnbm': 59}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
