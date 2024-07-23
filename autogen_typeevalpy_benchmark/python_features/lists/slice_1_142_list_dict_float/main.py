# A new list is created as a slice of another one containing functions.


def func1():
    return [52, 59, 39]


def func2():
    return {'lnbxk': 89, 'vhdua': 76, 'oxdex': 35}


def func3():
    return 41.04


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
