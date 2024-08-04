# Functions are assigned as elements of a list and then called.


def func1():
    return {'qlgar': 55, 'ctrvr': 65, 'feaxm': 37}


def func2():
    return [57, 30, 6]


def func3():
    return 70


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'cpbif'


b = ["Hello"]
b[0] = func4

f = b[0]()
