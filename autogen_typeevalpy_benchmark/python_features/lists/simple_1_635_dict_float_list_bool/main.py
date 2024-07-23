# Functions are assigned as elements of a list and then called.


def func1():
    return {'ycwnk': 47, 'xuerb': 75, 'qhnyj': 81}


def func2():
    return 86.55


def func3():
    return [3, 29, 57]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
