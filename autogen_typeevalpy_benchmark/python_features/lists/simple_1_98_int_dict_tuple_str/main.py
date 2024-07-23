# Functions are assigned as elements of a list and then called.


def func1():
    return 18


def func2():
    return {'hzfht': 33, 'gyuiv': 77, 'zwung': 64}


def func3():
    return (50, 34, 29)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'bbioo'


b = ["Hello"]
b[0] = func4

f = b[0]()
