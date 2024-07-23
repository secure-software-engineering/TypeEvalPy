# Functions are assigned as elements of a list and then called.


def func1():
    return {'jsnkr': 75, 'wnjzc': 56, 'xevyq': 61}


def func2():
    return (23, 98, 21)


def func3():
    return 85


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 66.09


b = ["Hello"]
b[0] = func4

f = b[0]()
