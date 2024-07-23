# Functions are assigned as elements of a list and then called.


def func1():
    return (68, 75, 31)


def func2():
    return [26, 36, 15]


def func3():
    return {'jvsmi': 44, 'mrmiw': 85, 'aljwj': 19}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 63


b = ["Hello"]
b[0] = func4

f = b[0]()
