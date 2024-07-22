# Functions are assigned as elements of a list and then called.


def func1():
    return 'dptlj'


def func2():
    return 75.32


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'rehvl': 46, 'xrfmo': 10, 'yrcmc': 23}


b = ["Hello"]
b[0] = func4

f = b[0]()
