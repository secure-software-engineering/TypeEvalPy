# Functions are assigned as elements of a list and then called.


def func1():
    return [44, 51, 72]


def func2():
    return 34.06


def func3():
    return 'bstji'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'omnkr': 32, 'xeyuy': 17, 'sowkp': 87}


b = ["Hello"]
b[0] = func4

f = b[0]()
