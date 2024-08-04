# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return {'hfmhb': 14, 'hdymt': 99, 'giktw': 43}


def func3():
    return 45


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'kqxxp'


b = ["Hello"]
b[0] = func4

f = b[0]()
