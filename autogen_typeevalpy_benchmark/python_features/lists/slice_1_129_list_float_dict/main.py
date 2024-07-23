# A new list is created as a slice of another one containing functions.


def func1():
    return [8, 45, 62]


def func2():
    return 75.31


def func3():
    return {'hrudn': 46, 'gggkb': 93, 'rxynt': 24}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
