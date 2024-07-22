# A new list is created as a slice of another one containing functions.


def func1():
    return {'pksqo': 89, 'nzdkb': 56, 'vcoui': 61}


def func2():
    return 71


def func3():
    return (47, 85, 65)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
