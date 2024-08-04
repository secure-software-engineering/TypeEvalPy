# Functions are assigned as elements of a list and then called.


def func1():
    return 'kcezm'


def func2():
    return [82, 84, 93]


def func3():
    return {'hpajf': 14, 'cngje': 43, 'ofriv': 89}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 69


b = ["Hello"]
b[0] = func4

f = b[0]()
