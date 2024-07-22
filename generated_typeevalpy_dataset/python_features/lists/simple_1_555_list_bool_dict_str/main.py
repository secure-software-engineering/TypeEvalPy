# Functions are assigned as elements of a list and then called.


def func1():
    return [46, 69, 64]


def func2():
    return True


def func3():
    return {'hzkkw': 42, 'zaank': 42, 'kcpas': 47}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'uoiur'


b = ["Hello"]
b[0] = func4

f = b[0]()
