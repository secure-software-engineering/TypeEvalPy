# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return {'qrjei': 17, 'faimq': 95, 'wnuqd': 7}


def func3():
    return 'akusq'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [62, 83, 58]


b = ["Hello"]
b[0] = func4

f = b[0]()
