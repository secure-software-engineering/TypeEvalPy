# Functions are assigned as elements of a list and then called.


def func1():
    return 'ckqob'


def func2():
    return [52, 57, 90]


def func3():
    return {'jjeek': 90, 'dlujw': 64, 'delqz': 43}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 85.62


b = ["Hello"]
b[0] = func4

f = b[0]()
