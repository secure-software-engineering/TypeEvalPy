# Functions are assigned as elements of a list and then called.


def func1():
    return (17, 58, 57)


def func2():
    return [90, 20, 31]


def func3():
    return {'ykzvm': 24, 'pdipu': 36, 'pbdil': 6}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'zdfno'


b = ["Hello"]
b[0] = func4

f = b[0]()
