# Functions are assigned as elements of a list and then called.


def func1():
    return {'izxyy': 14, 'imiqj': 49, 'wdnvd': 46}


def func2():
    return [69, 52, 81]


def func3():
    return 24


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 68.42


b = ["Hello"]
b[0] = func4

f = b[0]()
