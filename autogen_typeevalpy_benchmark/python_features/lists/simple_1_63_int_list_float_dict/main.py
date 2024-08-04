# Functions are assigned as elements of a list and then called.


def func1():
    return 35


def func2():
    return [98, 39, 50]


def func3():
    return 90.88


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'zcsru': 18, 'rbylp': 5, 'rvpcc': 24}


b = ["Hello"]
b[0] = func4

f = b[0]()
