# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return {'jxwdc': 46, 'cojgb': 91, 'wkomc': 85}


def func3():
    return 51


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 58.42


b = ["Hello"]
b[0] = func4

f = b[0]()
