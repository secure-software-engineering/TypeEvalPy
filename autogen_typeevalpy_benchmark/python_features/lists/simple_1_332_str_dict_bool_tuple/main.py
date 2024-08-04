# Functions are assigned as elements of a list and then called.


def func1():
    return 'urxmf'


def func2():
    return {'sdxwx': 27, 'mzlga': 40, 'qtgay': 98}


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (33, 20, 44)


b = ["Hello"]
b[0] = func4

f = b[0]()
