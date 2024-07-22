# Functions are assigned as elements of a list and then called.


def func1():
    return 'kijwm'


def func2():
    return {'ihutd': 84, 'wndkk': 5, 'pxven': 6}


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [84, 60, 39]


b = ["Hello"]
b[0] = func4

f = b[0]()
