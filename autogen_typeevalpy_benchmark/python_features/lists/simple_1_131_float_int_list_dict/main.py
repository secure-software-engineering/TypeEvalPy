# Functions are assigned as elements of a list and then called.


def func1():
    return 67.21


def func2():
    return 4


def func3():
    return [55, 55, 23]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'jscle': 75, 'afvld': 17, 'phyen': 55}


b = ["Hello"]
b[0] = func4

f = b[0]()
