# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return 'onyfp'


def func3():
    return {'zwxnx': 50, 'cvwki': 27, 'ttbym': 7}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [4, 53, 35]


b = ["Hello"]
b[0] = func4

f = b[0]()
