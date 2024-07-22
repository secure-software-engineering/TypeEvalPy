# Functions are assigned as elements of a list and then called.


def func1():
    return {'olatm': 25, 'ndnlp': 22, 'nemog': 19}


def func2():
    return [61, 18, 62]


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 55.62


b = ["Hello"]
b[0] = func4

f = b[0]()
