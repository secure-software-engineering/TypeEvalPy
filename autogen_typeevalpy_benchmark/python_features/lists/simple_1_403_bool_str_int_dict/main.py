# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return 'yhdwc'


def func3():
    return 42


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'jaqpa': 68, 'zvtfq': 89, 'inqpr': 9}


b = ["Hello"]
b[0] = func4

f = b[0]()
