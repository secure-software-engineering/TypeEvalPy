# Functions are assigned as elements of a list and then called.


def func1():
    return 34.73


def func2():
    return True


def func3():
    return {'lsidw': 65, 'vposy': 56, 'trdel': 22}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 60


b = ["Hello"]
b[0] = func4

f = b[0]()
