# Functions are assigned as elements of a list and then called.


def func1():
    return {'uipfq': 30, 'chhhv': 54, 'trlyx': 72}


def func2():
    return True


def func3():
    return (73, 96, 71)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'baqkk'


b = ["Hello"]
b[0] = func4

f = b[0]()
