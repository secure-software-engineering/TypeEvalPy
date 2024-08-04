# A new list is created as a slice of another one containing functions.


def func1():
    return [57, 31, 95]


def func2():
    return {'fqhmi': 79, 'eoywq': 8, 'xskmv': 25}


def func3():
    return True


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
