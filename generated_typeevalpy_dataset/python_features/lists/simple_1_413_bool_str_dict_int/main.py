# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return 'boyuq'


def func3():
    return {'qfutw': 50, 'ydhzn': 88, 'mkzqp': 96}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 22


b = ["Hello"]
b[0] = func4

f = b[0]()
