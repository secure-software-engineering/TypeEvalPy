# Functions are assigned as elements of a list and then called.


def func1():
    return 'ndhee'


def func2():
    return [16, 41, 29]


def func3():
    return 16.04


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'invsd': 70, 'vjasx': 95, 'jdyor': 58}


b = ["Hello"]
b[0] = func4

f = b[0]()
