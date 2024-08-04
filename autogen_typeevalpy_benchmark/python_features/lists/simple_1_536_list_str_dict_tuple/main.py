# Functions are assigned as elements of a list and then called.


def func1():
    return [57, 19, 72]


def func2():
    return 'ketlx'


def func3():
    return {'mcyxe': 41, 'zvdzu': 11, 'uiyos': 50}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (37, 38, 13)


b = ["Hello"]
b[0] = func4

f = b[0]()
