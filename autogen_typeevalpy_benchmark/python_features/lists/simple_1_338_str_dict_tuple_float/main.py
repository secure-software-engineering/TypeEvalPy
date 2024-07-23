# Functions are assigned as elements of a list and then called.


def func1():
    return 'mytfl'


def func2():
    return {'glwml': 26, 'uxbyp': 62, 'bbljq': 37}


def func3():
    return (83, 81, 90)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 44.62


b = ["Hello"]
b[0] = func4

f = b[0]()
