# Functions are assigned as elements of a list and then called.


def func1():
    return 29


def func2():
    return False


def func3():
    return {'jcbgq': 100, 'xssat': 31, 'qsiyf': 69}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (52, 46, 5)


b = ["Hello"]
b[0] = func4

f = b[0]()
