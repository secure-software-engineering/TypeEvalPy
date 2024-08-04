# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return {'drrwi': 86, 'bcfnf': 61, 'rphqc': 24}


def func3():
    return (77, 11, 77)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 32


b = ["Hello"]
b[0] = func4

f = b[0]()
