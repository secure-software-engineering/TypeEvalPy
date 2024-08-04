# Functions are assigned as elements of a list and then called.


def func1():
    return 'kawph'


def func2():
    return 76.68


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'bcdwd': 51, 'yjlzz': 15, 'emymk': 49}


b = ["Hello"]
b[0] = func4

f = b[0]()
