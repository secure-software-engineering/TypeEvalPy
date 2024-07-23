# Functions are assigned as elements of a list and then called.


def func1():
    return 'jlidf'


def func2():
    return False


def func3():
    return (74, 13, 64)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'qoimr': 66, 'bkijv': 21, 'wwmrw': 70}


b = ["Hello"]
b[0] = func4

f = b[0]()
