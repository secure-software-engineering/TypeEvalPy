# Functions are assigned as elements of a list and then called.


def func1():
    return 'ofagm'


def func2():
    return False


def func3():
    return [68, 14, 35]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'rrwiw': 92, 'ynskm': 45, 'caiic': 99}


b = ["Hello"]
b[0] = func4

f = b[0]()
