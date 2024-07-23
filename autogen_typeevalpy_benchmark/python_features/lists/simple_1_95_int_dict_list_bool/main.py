# Functions are assigned as elements of a list and then called.


def func1():
    return 94


def func2():
    return {'hpzii': 8, 'onzed': 37, 'bwdnc': 54}


def func3():
    return [27, 49, 89]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
