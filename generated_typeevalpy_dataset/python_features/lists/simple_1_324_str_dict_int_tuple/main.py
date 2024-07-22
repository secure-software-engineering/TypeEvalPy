# Functions are assigned as elements of a list and then called.


def func1():
    return 'szkay'


def func2():
    return {'sdtxq': 27, 'bhgoc': 90, 'mcste': 23}


def func3():
    return 92


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (54, 57, 39)


b = ["Hello"]
b[0] = func4

f = b[0]()
