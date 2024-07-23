# Functions are assigned as elements of a list and then called.


def func1():
    return [7, 56, 53]


def func2():
    return {'mccgb': 72, 'huaha': 72, 'rpjbc': 7}


def func3():
    return 'psimt'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 31


b = ["Hello"]
b[0] = func4

f = b[0]()
