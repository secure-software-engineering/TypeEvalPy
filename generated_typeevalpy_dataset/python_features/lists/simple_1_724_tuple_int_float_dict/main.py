# Functions are assigned as elements of a list and then called.


def func1():
    return (41, 26, 12)


def func2():
    return 68


def func3():
    return 44.14


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'gpeft': 86, 'ssbbr': 17, 'mvacp': 82}


b = ["Hello"]
b[0] = func4

f = b[0]()
