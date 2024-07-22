# Functions are assigned as elements of a list and then called.


def func1():
    return 43.36


def func2():
    return 'mdzie'


def func3():
    return [76, 29, 61]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'lugwf': 10, 'exnpb': 41, 'clcpq': 12}


b = ["Hello"]
b[0] = func4

f = b[0]()
