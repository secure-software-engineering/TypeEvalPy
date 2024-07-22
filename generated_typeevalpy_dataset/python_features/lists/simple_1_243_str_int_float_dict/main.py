# Functions are assigned as elements of a list and then called.


def func1():
    return 'mrhas'


def func2():
    return 36


def func3():
    return 89.46


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'riamb': 33, 'sjxcf': 44, 'phxcw': 7}


b = ["Hello"]
b[0] = func4

f = b[0]()
