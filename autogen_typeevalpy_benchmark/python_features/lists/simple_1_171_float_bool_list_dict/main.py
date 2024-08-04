# Functions are assigned as elements of a list and then called.


def func1():
    return 2.51


def func2():
    return True


def func3():
    return [61, 74, 92]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'bxgsi': 63, 'jmlkp': 16, 'sdflc': 96}


b = ["Hello"]
b[0] = func4

f = b[0]()
