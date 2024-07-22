# Functions are assigned as elements of a list and then called.


def func1():
    return [28, 64, 59]


def func2():
    return 'icynu'


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'oyvyp': 92, 'bdzct': 50, 'ycksn': 76}


b = ["Hello"]
b[0] = func4

f = b[0]()
