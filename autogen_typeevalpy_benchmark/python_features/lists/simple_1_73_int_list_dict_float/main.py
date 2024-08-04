# Functions are assigned as elements of a list and then called.


def func1():
    return 42


def func2():
    return [84, 78, 57]


def func3():
    return {'bfcvs': 30, 'knmdb': 74, 'hkhpu': 36}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 96.67


b = ["Hello"]
b[0] = func4

f = b[0]()
