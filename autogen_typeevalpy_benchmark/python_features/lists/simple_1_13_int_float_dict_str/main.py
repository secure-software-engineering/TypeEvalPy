# Functions are assigned as elements of a list and then called.


def func1():
    return 57


def func2():
    return 74.97


def func3():
    return {'jcqts': 66, 'mzzoe': 23, 'nyfss': 40}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'qwvhg'


b = ["Hello"]
b[0] = func4

f = b[0]()
