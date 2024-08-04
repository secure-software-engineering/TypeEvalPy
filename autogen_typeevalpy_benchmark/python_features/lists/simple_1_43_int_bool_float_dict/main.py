# Functions are assigned as elements of a list and then called.


def func1():
    return 95


def func2():
    return True


def func3():
    return 96.7


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'rerfx': 35, 'hzfuf': 49, 'myxkm': 50}


b = ["Hello"]
b[0] = func4

f = b[0]()
