# Functions are assigned as elements of a list and then called.


def func1():
    return 88.08


def func2():
    return True


def func3():
    return {'lgurk': 90, 'mnlqw': 16, 'rdbiv': 56}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'gzhfi'


b = ["Hello"]
b[0] = func4

f = b[0]()
