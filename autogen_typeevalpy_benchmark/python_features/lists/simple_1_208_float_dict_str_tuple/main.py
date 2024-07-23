# Functions are assigned as elements of a list and then called.


def func1():
    return 86.72


def func2():
    return {'nkzqc': 86, 'txaoh': 14, 'qufam': 31}


def func3():
    return 'zgwed'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (91, 10, 41)


b = ["Hello"]
b[0] = func4

f = b[0]()
