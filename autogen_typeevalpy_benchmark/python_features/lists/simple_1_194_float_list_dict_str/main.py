# Functions are assigned as elements of a list and then called.


def func1():
    return 7.09


def func2():
    return [87, 95, 63]


def func3():
    return {'mkrdf': 69, 'erqqh': 46, 'hwati': 58}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'npwkf'


b = ["Hello"]
b[0] = func4

f = b[0]()
