# Functions are assigned as elements of a list and then called.


def func1():
    return (74, 4, 49)


def func2():
    return False


def func3():
    return {'goufm': 16, 'emdgd': 74, 'btjhv': 28}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 10


b = ["Hello"]
b[0] = func4

f = b[0]()
