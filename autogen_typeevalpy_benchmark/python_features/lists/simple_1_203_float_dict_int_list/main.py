# Functions are assigned as elements of a list and then called.


def func1():
    return 52.43


def func2():
    return {'lltyy': 41, 'mhitj': 84, 'wybgb': 4}


def func3():
    return 50


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [32, 17, 66]


b = ["Hello"]
b[0] = func4

f = b[0]()
