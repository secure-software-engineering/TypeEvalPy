# A new list is created as a slice of another one containing functions.


def func1():
    return 59.39


def func2():
    return 16


def func3():
    return {'icklk': 80, 'vyvhq': 60, 'lself': 70}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
