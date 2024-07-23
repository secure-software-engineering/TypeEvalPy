# Functions are assigned as elements of a list and then called.


def func1():
    return {'beqel': 29, 'tgvkt': 27, 'lryvh': 13}


def func2():
    return False


def func3():
    return 30


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [56, 97, 49]


b = ["Hello"]
b[0] = func4

f = b[0]()
