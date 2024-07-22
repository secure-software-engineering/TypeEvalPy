# Functions are assigned as elements of a list and then called.


def func1():
    return (57, 62, 64)


def func2():
    return 37


def func3():
    return {'agrpr': 94, 'vngbk': 29, 'fkzek': 83}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
