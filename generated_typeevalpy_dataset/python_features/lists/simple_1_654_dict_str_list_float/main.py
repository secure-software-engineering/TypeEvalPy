# Functions are assigned as elements of a list and then called.


def func1():
    return {'jihza': 50, 'xdaqi': 57, 'djlhm': 84}


def func2():
    return 'ngxsn'


def func3():
    return [31, 30, 36]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 81.06


b = ["Hello"]
b[0] = func4

f = b[0]()
