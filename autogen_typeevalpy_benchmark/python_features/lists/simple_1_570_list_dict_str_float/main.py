# Functions are assigned as elements of a list and then called.


def func1():
    return [39, 66, 11]


def func2():
    return {'udjmn': 30, 'qqrfe': 39, 'uysfg': 56}


def func3():
    return 'iasdw'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 52.05


b = ["Hello"]
b[0] = func4

f = b[0]()
