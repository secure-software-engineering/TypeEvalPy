# Functions are assigned as elements of a list and then called.


def func1():
    return 'txnrc'


def func2():
    return True


def func3():
    return 46.59


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (99, 76, 57)


b = ["Hello"]
b[0] = func4

f = b[0]()
