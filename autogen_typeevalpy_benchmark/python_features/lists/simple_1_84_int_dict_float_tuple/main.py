# Functions are assigned as elements of a list and then called.


def func1():
    return 22


def func2():
    return {'pdwfq': 54, 'dugbv': 48, 'yppmr': 93}


def func3():
    return 63.03


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (38, 14, 89)


b = ["Hello"]
b[0] = func4

f = b[0]()
