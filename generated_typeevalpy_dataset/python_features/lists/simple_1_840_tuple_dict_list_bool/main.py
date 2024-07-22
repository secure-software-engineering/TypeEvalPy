# Functions are assigned as elements of a list and then called.


def func1():
    return (92, 72, 24)


def func2():
    return {'ecavy': 54, 'llvnf': 50, 'ngxjh': 76}


def func3():
    return [47, 86, 76]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
