# Functions are assigned as elements of a list and then called.


def func1():
    return [44, 1, 62]


def func2():
    return {'vbtbw': 97, 'oyriz': 78, 'gllcx': 95}


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (96, 23, 89)


b = ["Hello"]
b[0] = func4

f = b[0]()
