# Functions are assigned as elements of a list and then called.


def func1():
    return 14.06


def func2():
    return {'jzshx': 82, 'cwwul': 78, 'bhijx': 22}


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [82, 3, 98]


b = ["Hello"]
b[0] = func4

f = b[0]()
