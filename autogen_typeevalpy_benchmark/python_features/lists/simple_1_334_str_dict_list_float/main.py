# Functions are assigned as elements of a list and then called.


def func1():
    return 'bovwm'


def func2():
    return {'nnhpd': 50, 'jvjlg': 21, 'zlhur': 40}


def func3():
    return [72, 3, 2]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 71.16


b = ["Hello"]
b[0] = func4

f = b[0]()
