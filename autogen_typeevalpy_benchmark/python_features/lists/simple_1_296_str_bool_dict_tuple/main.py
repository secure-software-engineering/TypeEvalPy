# Functions are assigned as elements of a list and then called.


def func1():
    return 'rvkub'


def func2():
    return True


def func3():
    return {'nkxla': 14, 'bnnwj': 29, 'rhhqc': 13}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (20, 46, 38)


b = ["Hello"]
b[0] = func4

f = b[0]()
