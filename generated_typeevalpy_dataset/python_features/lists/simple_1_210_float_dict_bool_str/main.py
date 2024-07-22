# Functions are assigned as elements of a list and then called.


def func1():
    return 60.79


def func2():
    return {'favvz': 65, 'uqesj': 100, 'yqyjs': 85}


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'iltja'


b = ["Hello"]
b[0] = func4

f = b[0]()
