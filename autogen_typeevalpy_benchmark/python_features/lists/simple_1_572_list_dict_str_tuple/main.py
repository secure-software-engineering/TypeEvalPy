# Functions are assigned as elements of a list and then called.


def func1():
    return [9, 13, 38]


def func2():
    return {'xkmed': 75, 'mmejo': 77, 'tgbfi': 51}


def func3():
    return 'yffcd'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (100, 10, 93)


b = ["Hello"]
b[0] = func4

f = b[0]()
