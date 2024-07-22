# A new list is created as a slice of another one containing functions.


def func1():
    return {'mdtxo': 94, 'kzlmy': 51, 'srijk': 24}


def func2():
    return [61, 63, 51]


def func3():
    return 25


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
