# Functions are assigned as elements of a list and then called.


def func1():
    return (7, 96, 79)


def func2():
    return False


def func3():
    return [99, 80, 92]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'imoyi': 23, 'zsbwu': 100, 'tazud': 5}


b = ["Hello"]
b[0] = func4

f = b[0]()
