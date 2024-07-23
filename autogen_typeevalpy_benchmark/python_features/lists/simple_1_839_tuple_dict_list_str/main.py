# Functions are assigned as elements of a list and then called.


def func1():
    return (7, 86, 19)


def func2():
    return {'qndgj': 8, 'fcusw': 21, 'gaxvu': 54}


def func3():
    return [84, 58, 96]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'cnrfk'


b = ["Hello"]
b[0] = func4

f = b[0]()
