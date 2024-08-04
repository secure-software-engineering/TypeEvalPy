# Functions are assigned as elements of a list and then called.


def func1():
    return 64.78


def func2():
    return 'tbjfv'


def func3():
    return 45


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'qcyeg': 85, 'ytciz': 84, 'yqlgy': 35}


b = ["Hello"]
b[0] = func4

f = b[0]()
