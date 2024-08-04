# Functions are assigned as elements of a list and then called.


def func1():
    return 'tkbnp'


def func2():
    return 63


def func3():
    return {'jivfm': 74, 'pmonc': 71, 'snbkc': 97}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (65, 71, 58)


b = ["Hello"]
b[0] = func4

f = b[0]()
