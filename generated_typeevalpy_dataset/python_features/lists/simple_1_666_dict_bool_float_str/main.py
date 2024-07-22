# Functions are assigned as elements of a list and then called.


def func1():
    return {'krjeh': 96, 'hysij': 55, 'heksf': 46}


def func2():
    return False


def func3():
    return 85.0


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'pzelr'


b = ["Hello"]
b[0] = func4

f = b[0]()
