# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return {'bgszm': 44, 'xocle': 37, 'uwgnw': 36}


def func3():
    return (17, 3, 19)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [92, 41, 48]


b = ["Hello"]
b[0] = func4

f = b[0]()
