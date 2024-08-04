# Functions are assigned as elements of a list and then called.


def func1():
    return {'yadvi': 89, 'ooyia': 11, 'xdmae': 31}


def func2():
    return 'usenx'


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 50


b = ["Hello"]
b[0] = func4

f = b[0]()
