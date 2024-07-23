# Functions are assigned as elements of a list and then called.


def func1():
    return 49


def func2():
    return [42, 64, 67]


def func3():
    return 42.54


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'eauvl': 74, 'nkumh': 24, 'epvmt': 98}


b = ["Hello"]
b[0] = func4

f = b[0]()
