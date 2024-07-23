# Functions are assigned as elements of a list and then called.


def func1():
    return 'fatlf'


def func2():
    return 5.47


def func3():
    return {'wtzxn': 76, 'wjpij': 42, 'lcpam': 80}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (33, 76, 2)


b = ["Hello"]
b[0] = func4

f = b[0]()
