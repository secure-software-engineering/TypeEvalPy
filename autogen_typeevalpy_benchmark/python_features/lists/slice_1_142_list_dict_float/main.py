# A new list is created as a slice of another one containing functions.


def func1():
    return [44, 57, 39]


def func2():
    return {'zmmci': 82, 'hojgd': 13, 'gkkcn': 42}


def func3():
    return 92.12


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
