# Functions are assigned as elements of a list and then called.


def func1():
    return 'udfdq'


def func2():
    return (72, 13, 51)


def func3():
    return [11, 30, 59]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'qpinw': 67, 'afvdm': 54, 'hfidh': 28}


b = ["Hello"]
b[0] = func4

f = b[0]()
