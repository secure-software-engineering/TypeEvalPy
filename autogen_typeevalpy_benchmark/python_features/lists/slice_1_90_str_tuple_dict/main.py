# A new list is created as a slice of another one containing functions.


def func1():
    return 'mrwts'


def func2():
    return (23, 99, 68)


def func3():
    return {'haepv': 8, 'mqyol': 40, 'xncwp': 55}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
