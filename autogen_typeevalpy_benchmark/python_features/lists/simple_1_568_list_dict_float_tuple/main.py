# Functions are assigned as elements of a list and then called.


def func1():
    return [33, 11, 61]


def func2():
    return {'dhtkf': 38, 'tpjkb': 78, 'jyczd': 4}


def func3():
    return 5.7


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (50, 26, 15)


b = ["Hello"]
b[0] = func4

f = b[0]()
