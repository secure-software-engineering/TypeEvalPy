# Functions are assigned as elements of a list and then called.


def func1():
    return 44.18


def func2():
    return {'mivno': 65, 'uvtdg': 56, 'rlsft': 81}


def func3():
    return (73, 51, 82)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'cqdgs'


b = ["Hello"]
b[0] = func4

f = b[0]()
