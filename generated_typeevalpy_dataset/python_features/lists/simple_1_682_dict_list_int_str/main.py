# Functions are assigned as elements of a list and then called.


def func1():
    return {'wpwnq': 46, 'zgnte': 45, 'zwxkh': 70}


def func2():
    return [95, 32, 56]


def func3():
    return 5


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'iqopb'


b = ["Hello"]
b[0] = func4

f = b[0]()
