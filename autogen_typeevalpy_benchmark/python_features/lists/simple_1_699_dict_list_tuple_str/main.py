# Functions are assigned as elements of a list and then called.


def func1():
    return {'ntolu': 97, 'azdxl': 48, 'aojzl': 20}


def func2():
    return [9, 81, 86]


def func3():
    return (17, 20, 46)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'kgfkd'


b = ["Hello"]
b[0] = func4

f = b[0]()
