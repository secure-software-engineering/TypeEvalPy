# Functions are assigned as elements of a list and then called.


def func1():
    return [18, 6, 56]


def func2():
    return False


def func3():
    return 'mzwqj'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'pfalr': 18, 'mgzvx': 73, 'ytnak': 34}


b = ["Hello"]
b[0] = func4

f = b[0]()
