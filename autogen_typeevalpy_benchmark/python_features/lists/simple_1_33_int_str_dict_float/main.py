# Functions are assigned as elements of a list and then called.


def func1():
    return 82


def func2():
    return 'grgvu'


def func3():
    return {'tmjuu': 93, 'myblg': 69, 'vnoyw': 69}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 66.27


b = ["Hello"]
b[0] = func4

f = b[0]()
