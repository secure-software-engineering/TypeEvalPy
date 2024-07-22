# Functions are assigned as elements of a list and then called.


def func1():
    return 99


def func2():
    return 'lgpum'


def func3():
    return {'btgea': 11, 'hlxpy': 52, 'islzf': 92}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 45.11


b = ["Hello"]
b[0] = func4

f = b[0]()
