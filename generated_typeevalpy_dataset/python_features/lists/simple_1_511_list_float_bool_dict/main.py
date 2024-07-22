# Functions are assigned as elements of a list and then called.


def func1():
    return [29, 87, 59]


def func2():
    return 89.1


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'umeyk': 97, 'jxuui': 14, 'eblrv': 69}


b = ["Hello"]
b[0] = func4

f = b[0]()
