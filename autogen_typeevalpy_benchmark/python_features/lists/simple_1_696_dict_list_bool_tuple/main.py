# Functions are assigned as elements of a list and then called.


def func1():
    return {'srxbb': 55, 'vuhqj': 37, 'ywsav': 19}


def func2():
    return [22, 32, 50]


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (89, 6, 36)


b = ["Hello"]
b[0] = func4

f = b[0]()
