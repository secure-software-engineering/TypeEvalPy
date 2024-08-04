# Functions are assigned as elements of a list and then called.


def func1():
    return (23, 84, 15)


def func2():
    return {'noogy': 53, 'wrhdx': 53, 'guomq': 100}


def func3():
    return 'dnmtc'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
