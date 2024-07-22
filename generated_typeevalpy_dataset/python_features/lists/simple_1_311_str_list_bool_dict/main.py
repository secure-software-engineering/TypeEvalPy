# Functions are assigned as elements of a list and then called.


def func1():
    return 'vwucu'


def func2():
    return [57, 19, 13]


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'rvmwj': 81, 'mrnua': 43, 'vbxgl': 3}


b = ["Hello"]
b[0] = func4

f = b[0]()
