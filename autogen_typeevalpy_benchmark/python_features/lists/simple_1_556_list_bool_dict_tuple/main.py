# Functions are assigned as elements of a list and then called.


def func1():
    return [96, 40, 45]


def func2():
    return True


def func3():
    return {'uudmj': 39, 'xosnz': 54, 'cyhos': 84}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (57, 34, 70)


b = ["Hello"]
b[0] = func4

f = b[0]()
