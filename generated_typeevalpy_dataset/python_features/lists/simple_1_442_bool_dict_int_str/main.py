# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return {'xmwxv': 15, 'hyevn': 9, 'youlp': 89}


def func3():
    return 60


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'fwsro'


b = ["Hello"]
b[0] = func4

f = b[0]()
