# Functions are assigned as elements of a list and then called.


def func1():
    return {'kszkj': 89, 'trlsr': 64, 'imjev': 36}


def func2():
    return [5, 30, 67]


def func3():
    return 35


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'cehvs'


b = ["Hello"]
b[0] = func4

f = b[0]()
