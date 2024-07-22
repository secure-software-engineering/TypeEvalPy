# Functions are assigned as elements of a list and then called.


def func1():
    return 'qqrdb'


def func2():
    return 100


def func3():
    return {'heesx': 65, 'svnga': 22, 'rthqb': 44}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
