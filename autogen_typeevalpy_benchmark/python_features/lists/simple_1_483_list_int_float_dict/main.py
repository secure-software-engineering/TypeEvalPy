# Functions are assigned as elements of a list and then called.


def func1():
    return [61, 62, 21]


def func2():
    return 98


def func3():
    return 6.3


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'fomdn': 77, 'rdvts': 21, 'lkyjf': 67}


b = ["Hello"]
b[0] = func4

f = b[0]()
