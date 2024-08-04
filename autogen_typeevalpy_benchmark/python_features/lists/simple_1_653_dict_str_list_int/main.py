# Functions are assigned as elements of a list and then called.


def func1():
    return {'rcvpf': 12, 'dcimq': 38, 'zuvwr': 84}


def func2():
    return 'wqvsq'


def func3():
    return [39, 89, 91]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 16


b = ["Hello"]
b[0] = func4

f = b[0]()
