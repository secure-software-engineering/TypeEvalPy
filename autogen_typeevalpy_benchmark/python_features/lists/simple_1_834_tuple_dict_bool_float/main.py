# Functions are assigned as elements of a list and then called.


def func1():
    return (80, 76, 68)


def func2():
    return {'eshyl': 22, 'fcawx': 8, 'amrbp': 88}


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 72.08


b = ["Hello"]
b[0] = func4

f = b[0]()
