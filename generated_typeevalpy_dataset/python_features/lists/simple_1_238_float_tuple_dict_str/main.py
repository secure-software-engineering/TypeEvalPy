# Functions are assigned as elements of a list and then called.


def func1():
    return 96.96


def func2():
    return (79, 80, 13)


def func3():
    return {'xdkrt': 98, 'edccu': 97, 'mmiig': 48}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'tsaly'


b = ["Hello"]
b[0] = func4

f = b[0]()
