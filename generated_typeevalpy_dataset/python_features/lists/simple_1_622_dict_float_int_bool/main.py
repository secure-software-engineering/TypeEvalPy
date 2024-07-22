# Functions are assigned as elements of a list and then called.


def func1():
    return {'jhflx': 25, 'riuze': 51, 'eshcj': 87}


def func2():
    return 57.54


def func3():
    return 85


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
