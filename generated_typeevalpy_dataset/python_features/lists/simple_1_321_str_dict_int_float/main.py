# Functions are assigned as elements of a list and then called.


def func1():
    return 'jwrmx'


def func2():
    return {'pfibh': 96, 'jlnyg': 89, 'lpfnj': 27}


def func3():
    return 50


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 28.69


b = ["Hello"]
b[0] = func4

f = b[0]()
