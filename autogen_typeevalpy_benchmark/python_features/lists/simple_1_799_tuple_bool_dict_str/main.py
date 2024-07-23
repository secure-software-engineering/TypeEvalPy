# Functions are assigned as elements of a list and then called.


def func1():
    return (16, 45, 35)


def func2():
    return True


def func3():
    return {'dwccp': 94, 'jriep': 47, 'qpjlf': 63}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'sozvg'


b = ["Hello"]
b[0] = func4

f = b[0]()
