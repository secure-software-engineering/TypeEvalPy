# Functions are assigned as elements of a list and then called.


def func1():
    return 33


def func2():
    return (82, 94, 52)


def func3():
    return {'jufxc': 34, 'aqpwl': 97, 'yxhtz': 61}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 71.42


b = ["Hello"]
b[0] = func4

f = b[0]()
