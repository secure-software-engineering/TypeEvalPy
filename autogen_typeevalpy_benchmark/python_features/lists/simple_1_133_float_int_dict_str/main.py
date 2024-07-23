# Functions are assigned as elements of a list and then called.


def func1():
    return 74.44


def func2():
    return 80


def func3():
    return {'rrsru': 18, 'jmsoy': 15, 'nvrbj': 34}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'jfpzs'


b = ["Hello"]
b[0] = func4

f = b[0]()
