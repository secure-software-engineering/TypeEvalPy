# Functions are assigned as elements of a list and then called.


def func1():
    return (12, 30, 77)


def func2():
    return 'fxcxk'


def func3():
    return {'fdxgy': 12, 'spljl': 84, 'jcwcq': 70}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 23.09


b = ["Hello"]
b[0] = func4

f = b[0]()
