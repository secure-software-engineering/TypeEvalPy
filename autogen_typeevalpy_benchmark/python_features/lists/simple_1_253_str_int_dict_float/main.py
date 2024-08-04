# Functions are assigned as elements of a list and then called.


def func1():
    return 'fsezc'


def func2():
    return 50


def func3():
    return {'hakhr': 67, 'jgrec': 36, 'yjiri': 72}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 30.77


b = ["Hello"]
b[0] = func4

f = b[0]()
