# Functions are assigned as elements of a list and then called.


def func1():
    return {'geemd': 14, 'rjvse': 49, 'tjrft': 83}


def func2():
    return [77, 61, 33]


def func3():
    return 56


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
