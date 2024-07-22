# Functions are assigned as elements of a list and then called.


def func1():
    return {'dholz': 50, 'wzrdz': 86, 'yvole': 61}


def func2():
    return (76, 9, 35)


def func3():
    return 'xnotc'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 83.49


b = ["Hello"]
b[0] = func4

f = b[0]()
