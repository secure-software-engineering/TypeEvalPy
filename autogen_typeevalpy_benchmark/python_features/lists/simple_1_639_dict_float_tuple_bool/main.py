# Functions are assigned as elements of a list and then called.


def func1():
    return {'uzamj': 79, 'sdemd': 54, 'vowhy': 49}


def func2():
    return 91.71


def func3():
    return (7, 4, 85)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
