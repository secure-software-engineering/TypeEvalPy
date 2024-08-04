# Functions are assigned as elements of a list and then called.


def func1():
    return 'qasph'


def func2():
    return {'xuxpe': 19, 'gtmns': 6, 'wsnpq': 9}


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [88, 72, 77]


b = ["Hello"]
b[0] = func4

f = b[0]()
