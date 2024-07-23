# A new list is created as a slice of another one containing functions.


def func1():
    return 76


def func2():
    return {'uofoa': 9, 'xgfur': 12, 'twamb': 100}


def func3():
    return 74.9


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
