# Functions are assigned as elements of a list and then called.


def func1():
    return 'anqew'


def func2():
    return (48, 77, 95)


def func3():
    return {'jqriv': 61, 'vwhki': 65, 'giotx': 85}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [86, 24, 22]


b = ["Hello"]
b[0] = func4

f = b[0]()
