# Functions are assigned as elements of a list and then called.


def func1():
    return 'zffqt'


def func2():
    return [36, 96, 76]


def func3():
    return {'nkwkd': 18, 'ehuxd': 42, 'azpnl': 27}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (76, 48, 69)


b = ["Hello"]
b[0] = func4

f = b[0]()
