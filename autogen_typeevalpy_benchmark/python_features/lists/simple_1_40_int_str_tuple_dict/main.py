# Functions are assigned as elements of a list and then called.


def func1():
    return 59


def func2():
    return 'twzia'


def func3():
    return (8, 98, 33)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'hblvt': 21, 'rbxsx': 15, 'mluxe': 58}


b = ["Hello"]
b[0] = func4

f = b[0]()
