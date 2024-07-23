# Functions are assigned as elements of a list and then called.


def func1():
    return {'zedue': 10, 'hivrx': 88, 'amfgn': 38}


def func2():
    return 35.89


def func3():
    return 'mbqei'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [51, 53, 19]


b = ["Hello"]
b[0] = func4

f = b[0]()
