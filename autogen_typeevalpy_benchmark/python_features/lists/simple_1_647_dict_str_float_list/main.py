# Functions are assigned as elements of a list and then called.


def func1():
    return {'nyutt': 72, 'jabxy': 15, 'mhipw': 41}


def func2():
    return 'nmfga'


def func3():
    return 60.9


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [76, 88, 18]


b = ["Hello"]
b[0] = func4

f = b[0]()
