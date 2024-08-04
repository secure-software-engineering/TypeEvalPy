# Functions are assigned as elements of a list and then called.


def func1():
    return {'wfdio': 77, 'myeex': 21, 'ibqqg': 6}


def func2():
    return (8, 75, 13)


def func3():
    return 'uzsng'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 31.89


b = ["Hello"]
b[0] = func4

f = b[0]()
