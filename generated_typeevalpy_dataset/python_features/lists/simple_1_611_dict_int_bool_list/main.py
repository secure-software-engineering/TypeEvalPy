# Functions are assigned as elements of a list and then called.


def func1():
    return {'fkybl': 76, 'yinrn': 25, 'cwevq': 60}


def func2():
    return 38


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [4, 36, 32]


b = ["Hello"]
b[0] = func4

f = b[0]()
