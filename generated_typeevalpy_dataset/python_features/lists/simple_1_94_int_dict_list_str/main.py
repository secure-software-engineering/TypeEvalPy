# Functions are assigned as elements of a list and then called.


def func1():
    return 54


def func2():
    return {'ifwdk': 33, 'owdrw': 85, 'anxdw': 85}


def func3():
    return [69, 71, 57]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'nemha'


b = ["Hello"]
b[0] = func4

f = b[0]()
