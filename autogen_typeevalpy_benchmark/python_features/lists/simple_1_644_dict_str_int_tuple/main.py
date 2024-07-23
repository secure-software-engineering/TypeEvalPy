# Functions are assigned as elements of a list and then called.


def func1():
    return {'wluep': 37, 'muyqi': 63, 'zugih': 52}


def func2():
    return 'qwkak'


def func3():
    return 60


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (12, 36, 1)


b = ["Hello"]
b[0] = func4

f = b[0]()
