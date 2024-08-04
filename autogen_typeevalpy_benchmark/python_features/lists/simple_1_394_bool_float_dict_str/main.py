# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return 8.07


def func3():
    return {'gpmrf': 25, 'klyby': 77, 'sxmiy': 13}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'duumu'


b = ["Hello"]
b[0] = func4

f = b[0]()
