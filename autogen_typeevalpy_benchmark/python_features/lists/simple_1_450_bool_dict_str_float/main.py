# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return {'djkch': 46, 'suaev': 38, 'oyttg': 11}


def func3():
    return 'wjkmc'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 5.18


b = ["Hello"]
b[0] = func4

f = b[0]()
