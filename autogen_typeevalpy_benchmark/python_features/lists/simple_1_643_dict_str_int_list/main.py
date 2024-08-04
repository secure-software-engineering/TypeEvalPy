# Functions are assigned as elements of a list and then called.


def func1():
    return {'lppls': 32, 'argsx': 48, 'oxckf': 73}


def func2():
    return 'txagx'


def func3():
    return 59


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [58, 42, 97]


b = ["Hello"]
b[0] = func4

f = b[0]()
