# Functions are assigned as elements of a list and then called.


def func1():
    return 1.74


def func2():
    return 34


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'hclfg': 35, 'alhtk': 39, 'itfpq': 35}


b = ["Hello"]
b[0] = func4

f = b[0]()
