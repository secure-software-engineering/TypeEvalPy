# Functions are assigned as elements of a list and then called.


def func1():
    return {'sitnp': 34, 'vnpkd': 78, 'aqmyf': 22}


def func2():
    return [34, 92, 61]


def func3():
    return 1.92


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'voexb'


b = ["Hello"]
b[0] = func4

f = b[0]()
