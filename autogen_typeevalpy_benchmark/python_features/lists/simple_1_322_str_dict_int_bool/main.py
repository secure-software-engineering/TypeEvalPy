# Functions are assigned as elements of a list and then called.


def func1():
    return 'aopuq'


def func2():
    return {'szwpm': 33, 'dsndm': 55, 'nygjt': 86}


def func3():
    return 36


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
