# Functions are assigned as elements of a list and then called.


def func1():
    return [76, 2, 64]


def func2():
    return {'bnfoe': 17, 'ctsdm': 41, 'kxrod': 89}


def func3():
    return 57


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (98, 13, 54)


b = ["Hello"]
b[0] = func4

f = b[0]()
