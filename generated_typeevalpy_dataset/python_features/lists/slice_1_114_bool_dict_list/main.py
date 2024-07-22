# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return {'nhpxz': 69, 'mrrgu': 2, 'zmxnt': 33}


def func3():
    return [6, 36, 41]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
